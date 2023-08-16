from django.conf import settings
from .models import Product

class Cart(object):
    def __init__(self, request):
        # this allows the Cart object to access session data and be able to store items added and price of objects
        self.session = request.session
        # checks if the session contains an object with this ID
        cart = self.session.get(settings.CART_SESSION_ID)
        # if the cart value is None, this initializes an empty cart for the user
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    # iteration function
    def __iter__(self):
        # loops through all the keys in the session which are the products
        for p in self.cart.keys():
            # sets the product key inside the dictionary of the cart to the correct product obtained from the database
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.cart.values():
            # multiply the price of the object by the quantity and divides that number by 100, the cost is in cents
            item['total_price'] = int(item['product'].price * item['quantity'])

            yield item

    # length function
    def __len__(self):
        # calculates and returns the total quantity of items in the cart
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        # assigns the current cart to the session, this allows the cart data to stored
        self.session[settings.CART_SESSION_ID] = self.cart
        # This lets the server know the session has been modified and needs to be saved
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': int(quantity), 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove(product_id)

        self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_cost(self):
        # loop through the keys which are the products
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        # sums the price of the products times the quantity then divides each price by 100
        return int(sum(item['product'].price * item['quantity'] / 100 for item in self.cart.values()))


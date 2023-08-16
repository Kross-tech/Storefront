from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from .forms import OrderForm
from .models import Product, Category, Order, OrderItem

def add_to_cart(request, product_id):
    # creates a new instance of Cart
    cart = Cart(request)
    # adds the product id to the cart
    cart.add(product_id)

    return redirect('index')

def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(product_id, quantity, True)

    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('view_cart')

def view_cart(request):
    cart = Cart(request)

    return render(request, 'view_cart.html', {
        'cart': cart
    })

@login_required
def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            total_price = 0

            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])

            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = total_price
            order.save()

            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()

            return redirect('myaccount')
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {
        'cart': cart,
        'form': form,
    })

def product_detail(request, category_slug, slug):
    # returns a 404 error instead of a server error
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {
        'product': product
    })

def category_detail(request, slug):
    # returns a 404 error instead of a server error
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'category_detail.html', {
        'category': category,
        'products': products
    })

def shop(request):
    return render(request, 'shop.html')

def reviews(request):
    return render(request, 'reviews.html')

def faq(request):
    return render(request, 'faq.html')

def contact_us(request):
    return render(request, 'contact_us.html')

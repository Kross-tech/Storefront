from django.urls import path
from . import views


urlpatterns = [
    # matches an integer value and captures it as the product_id, then passes it as an argument to the add_to_cart function
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('change-quantity/<str:product_id>/', views.change_quantity, name='change_quantity'),
    path('remove-from-cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/checkout/', views.checkout, name='checkout'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
]

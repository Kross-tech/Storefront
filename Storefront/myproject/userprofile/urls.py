from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('myaccount/', views.myaccount, name='myaccount'),
    path('signup/', views.signup, name='signup'),
    # specify to use userprofile instead of the default registration/login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # uses a logout class in auth_views and renders it as a view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
]

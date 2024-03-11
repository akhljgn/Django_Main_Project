from store.forms import LoginForm, PasswordChangeForm
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'store'


urlpatterns = [
    path('', views.home, name="home"),
    
    #for Cart and Checkout
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('remove_cart/<int:cart_id>/', views.remove_cart, name="remove_cart"),
    path('plus_cart/<int:cart_id>/', views.plus_cart, name="plus_cart"),
    path('minus_cart/<int:cart_id>/', views.minus_cart, name="minus_cart"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('orders/', views.orders, name="orders"),

    #for Products
    path('product/<slug:slug>/', views.detail, name="product-detail"),
    path('categories/', views.all_categories, name="all-categories"),
    path('<slug:slug>/', views.category_products, name="category-products"),


    #for Authentication
    path('accounts/register/', views.RegistrationView.as_view(), name="register"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='account/signin.html', authentication_form=LoginForm), name="login"),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/add_address/', views.AddressView.as_view(), name="add_address"),
    path('accounts/remove_address/<int:id>/', views.remove_address, name="remove_address"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='store:login'), name="logout"),

    # for password change
    path('accounts/password-change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html', form_class=PasswordChangeForm, success_url='/accounts/password-change-done/'), name="password-change"),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name="password-change-done"),

]
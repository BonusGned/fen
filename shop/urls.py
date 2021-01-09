from django.contrib.auth.views import LogoutView
from django.urls import path


from cart.views import AddToCartView, DeleteFromCartView, ChangeQTYView, CheckoutView, CartListView
from customers.views import LoginView, RegistrationView, ProfileView
from orders.views import MakeOrderView
from . import views
from .views import ProductDetailView, CategoryDetailView

urlpatterns = [
    path('', views.BaseView.as_view(), name='home'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartListView.as_view(), name='cart_list'),
    # path('cart/add-to-cart/<int:product_id>/', cart_add, name='add_to_cart'),
    # path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('add-to-cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

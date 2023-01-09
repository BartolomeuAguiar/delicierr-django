from django.urls import path

from . import views

urlpatterns = [
    path('products/addorderitem/', views.AddOrderItemView.as_view(),
         name="add_order_item"
         ),
    path('products/removeorderitem/', views.RemoveOrderItemView.as_view(),
         name="remove_order_item"
         ),
    path('products/cart/', views.CartView.as_view(),
         name="cart"
         ),
]

from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.OrderListViewHome.as_view(),
         name="home"
         ),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(),
         name="show_order"
         ),
    path('orders/addorderitem/', views.AddOrderItemView.as_view(),
         name="add_order_item"
         ),
    path('orders/removeorderitem/', views.RemoveOrderItemView.as_view(),
         name="remove_order_item"
         ),
    path('orders/order/', views.OrderView.as_view(),
         name="order"
         ),
]

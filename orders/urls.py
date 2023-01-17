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
    path('orders/neworder/', views.ShowClientsToNewOrderView.as_view(),
         name="clients-new-order"
         ),
    path('orders/<int:pk>',
         views.create_order,
         name='order_create'
         ),

]

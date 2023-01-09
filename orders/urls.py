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
    path('orders/addorder/', views.AddOrderView.as_view(),
         name="new_order"
         ),

]

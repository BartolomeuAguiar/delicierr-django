from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('addorderitem/', views.AddOrderItemView.as_view(),
         name="add_order_item"
         ),
    path('removeorderitem/', views.RemoveOrderItemView.as_view(),
         name="remove_order_item"
         ),
    path('product/<int:pk>', views.ProductDetailView.as_view(),
         name="detail"
         ),
]

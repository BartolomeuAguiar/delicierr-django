from django.views.generic import ListView

from .models import Order

# Create your views here.


class OrderListViewHome(ListView):
    model = Order
    context_object_name = 'orders'
    ordering = ['pk']
    template_name = 'orders/pages/home.html'

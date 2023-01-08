from django.views.generic import ListView

from .models import Order

# Create your views here.


class OrderListViewHome(ListView):
    model = Order
    context_object_name = 'orders'
    ordering = ['delivery_date']
    template_name = 'orders/pages/home.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.exclude(
            status_order='CL',
        )
        return qs

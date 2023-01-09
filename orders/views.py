from django.views.generic import DetailView, ListView, View

from .models import Order

# Create your views here.


class OrderListViewBase(ListView):
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


class OrderListViewHome(OrderListViewBase):
    template_name = 'orders/pages/home.html'


class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/pages/order_detail.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.exclude(
            status_order='CL',
        )
        return qs


class AddOrderItemView(View):
    pass


class RemoveOrderItemView(View):
    pass


class OrderView(View):
    pass

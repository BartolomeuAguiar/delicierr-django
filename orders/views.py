from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from orders.forms import NewOrderForm

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


class NewOrderView(View):
    def get_order(self, id=None):
        order = None

        if id is not None:
            order = Order.objects.filter(
                pk=id
            ).first()

            if not order:
                raise Http404
        return order

    def render_order(self, form):
        return render(
            self.request,
            'orders/pages/new_order.html',
            context={
                'form': form
            }
        )

    def get(self, request, id=None):
        order = self.get_order(id)
        form = NewOrderForm(instance=order)
        return self.render_order(form)

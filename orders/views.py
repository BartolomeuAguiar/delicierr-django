from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from clients.models import Client
from products.models import Product

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


class ShowClientsToNewOrderView(View):
    def render_order(self):
        clients = Client.objects.all()

        return render(
            self.request,
            'orders/pages/clients.html',
            context={
                'clients': clients,
            }
        )

    def get(self, request, id=None):
        return self.render_order()


def create_order(request, pk):
    client = Client.objects.get(id=pk)
    produtos = Product.objects.all()
    carrinho = request.session.get('carrinho', {})
    # TODO criar template para mostrar produtos e adicionar ao carrinho
    context = {
        'cliente': client,
        'produtos': produtos,
        'carrinho': carrinho
    }
    return render(request, 'orders/pages/new_order_itens.html', context)

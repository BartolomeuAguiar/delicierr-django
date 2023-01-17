from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, View

from .models import Product, Variation

# Create your views here.


class AddOrderItemView(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('orders:home')
        )
        variation_id = self.request.GET.get('vid')

        variation = get_object_or_404(Variation, id=variation_id)
        variation_name = variation.name
        product = variation.product
        product_sabor = self.request.GET.get('orderitem_sabor')
        product_id = product.pk
        product_name = product.name
        product_price = variation.price
        product_amount = 1

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()

        carrinho = self.request.session['carrinho']

        if variation_id in carrinho:
            quantidade_carrinho = carrinho[variation_id]['product_amount']
            quantidade_carrinho += 1
            carrinho[variation_id]['product_amount'] = quantidade_carrinho
        else:
            carrinho[variation_id] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_id': variation_id,
                'variation_name': variation_name,
                'product_price': product_price,
                'product_amount': product_amount,
                'product_sabor': product_sabor,
            }
        self.request.session.save()

        messages.success(
            self.request,
            f'Produto {product_name} {variation_name} adicionado ao seu '
            f'carrinho {carrinho[variation_id]["product_amount"]}x.'
        )
        return redirect(http_referer)


class RemoveOrderItemView(View):
    pass


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'produto'
    template_name = 'products/pages/product_detail.html'

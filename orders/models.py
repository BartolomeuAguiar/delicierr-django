from django.db import models
from django.utils.translation import gettext_lazy as _

from clients.models import Client

# Create your models here.


class Order (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total = models.FloatField(default=0.0)
    delivery_date = models.DateTimeField(
        'Delivery Date', auto_now=False, auto_now_add=False)
    for_delivery = models.BooleanField()

    delivery_method = models.CharField(
        choices=(
            ('P', 'Própria'),
            ('T', 'App Terceirizado')
        ),
        max_length=1,
        blank=True
    )
    delivery_address = models.CharField(blank=True, max_length=300)
    comments = models.TextField(max_length=500, blank=True)
    status_order = models.CharField(
        choices=(
            ('CR', 'CREATED'),
            ('CL', 'CANCELED'),
            ('CF', 'CONFIRMED'),
            ('FN', 'FINISHED'),
        ),
        max_length=2,
        default='CR',
    )
    payment_form = models.CharField(
        _("Payment Form"),
        max_length=2,
        blank=True,
        choices=(
            ('CS', _('CASH')),
            ('CC', _('CREDIT CARD')),
            ('DC', _('DEBIT CARD')),
            ('PX', _('PIX')),
        ),
        default='PX',
    )
    status_payment = models.CharField(
        choices=(
            ('NP', 'NOT PAID'),
            ('PG', 'PAID'),
            ('PE', 'PAID ENTRY'),
        ),
        max_length=2,
        blank=True,
        default='NP',
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(f'{self.pk}-{self.delivery_date.year}')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=150)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=150)
    variation_id = models.PositiveIntegerField()
    sabor = models.CharField(max_length=50, blank=True, default=None)
    price = models.FloatField()
    price_additional = models.FloatField(blank=True, default=0.0)
    price_discount = models.FloatField(blank=True, default=0.0)
    amount = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Itens"

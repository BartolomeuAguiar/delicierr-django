from collections import defaultdict

from django import forms
from django.utils.translation import gettext_lazy as _

from orders.models import Order


class NewOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._my_errors = defaultdict(list)

    class Meta:
        model = Order
        fields = [
            'client',
            'total',
            'delivery_date',
            'for_delivery',
            'delivery_method',
            'delivery_address',
            'payment_form',
            'status_payment',
        ]
        widgets = {
            'delivery_method': forms.Select(
                choices=(
                    ('P', 'Própria'),
                    ('T', 'App Terceirizado'),
                ),
                attrs={
                    'class': 'form-control'
                }
            ),
            'payment_form': forms.Select(
                choices=(
                    ('CS', _('CASH')),
                    ('CC', _('CREDIT CARD')),
                    ('DC', _('DEBIT CARD')),
                    ('PX', _('PIX')),
                ),
                attrs={
                    'class': 'form-control'
                }
            ),
        }

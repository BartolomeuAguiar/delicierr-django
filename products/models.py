from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField('Title', max_length=50)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    active = models.BooleanField(_('Active'))
    name = models.CharField(_('Title'), max_length=150)
    description = models.CharField(
        _("Long Description"),
        max_length=300,
        blank=True
    )
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=150)
    price = models.FloatField()
    price_additional = models.FloatField(default=0.0, blank=True)
    price_discount = models.FloatField(default=0.0, blank=True)

    class Meta:
        verbose_name = _("variation")
        verbose_name_plural = _("variations")

    def __str__(self):
        return f'{self.product.name} {self.name}' or self.product.name

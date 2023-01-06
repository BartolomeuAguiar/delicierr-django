from django.contrib import admin

from .models import Category, Product, Variation

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    '''Admin View for Variation'''

    ordering = ('pk',)


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    ordering = ('name',)
    inlines = [
        VariationInline,
    ]

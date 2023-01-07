from django.contrib import admin

from .models import Perfil

# Register your models here.


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    '''Admin View for Perfil'''

    ordering = ('user',)

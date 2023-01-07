from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Perfil(models.Model):
    """Model definition for Perfil."""

    celphone = models.CharField(
        _("Celphone"),
        max_length=15,
        blank=True,
        unique=True
    )
    user = models.OneToOneField(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE
    )
    address = models.CharField(_("Address"), max_length=500, blank=True)
    birthday = models.DateField(
        _("Birthday"), auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for Perfil."""

        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfils'

    def __str__(self):
        """Unicode representation of Perfil."""
        return self.user.first_name or self.user.username

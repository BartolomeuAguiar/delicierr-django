from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Client(models.Model):
    """Model definition for Perfil."""
    name = models.CharField(_("Name"), max_length=300)
    celphone = models.CharField(
        _("Celphone"),
        max_length=15,
        blank=False,
        unique=True,
    )
    address = models.CharField(_("Address"), max_length=500, blank=True)
    birthday = models.DateField(
        _("Birthday"), auto_now=False, auto_now_add=False, blank=True)

    class Meta:
        """Meta definition for Perfil."""

        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        """Unicode representation of Perfil."""
        return self.name

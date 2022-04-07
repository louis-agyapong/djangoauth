from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    web_id = models.CharField(_("Web Id"), max_length=50, unique=True)
    slug = models.SlugField(_("Slug"), max_length=50)
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True)
    is_active = models.BooleanField(_("Is Active"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        app_label = "inventory"
        # permissions = (("view_product", "Can view product"),)

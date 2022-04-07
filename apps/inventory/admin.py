from django.contrib import admin
from django.http import HttpRequest
from django.utils import timezone

from .models import Product


class ReadOnlyAdminMixin:
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return super().has_view_permission(request, obj)


@admin.register(Product)
class ProductAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ("name", "web_id", "slug", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("web_id",)}

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superuser = request.user.is_superuser

    #     if not is_superuser:
    #         form.base_fields["name"].disabled = True
    #     return form

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        if request.user.has_perm("inventory.change_product"):
            return True
        else:
            return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        """user can view content from 9:00 to 17:00"""
        time_now = timezone.now()
        if time_now.hour >= 9 and time_now.hour <= 17:
            return True
        return False

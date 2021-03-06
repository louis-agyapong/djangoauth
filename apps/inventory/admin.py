from django.contrib import admin
from django.http import HttpRequest
from django.utils import timezone
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user

from .models import Product

# class ReadOnlyAdminMixin:
#     def has_add_permission(self, request: HttpRequest) -> bool:
#         return False

#     def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
#         return False

#     def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
#         return False

#     def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
#         return super().has_view_permission(request, obj)


# @admin.register(Product)
# class ProductAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
#     list_display = ("name", "web_id", "slug", "is_active")
#     list_filter = ("is_active",)
#     search_fields = ("name",)
#     prepopulated_fields = {"slug": ("web_id",)}

#     # def get_form(self, request, obj=None, **kwargs):
#     #     form = super().get_form(request, obj, **kwargs)
#     #     is_superuser = request.user.is_superuser

#     #     if not is_superuser:
#     #         form.base_fields["name"].disabled = True
#     #     return form

#     def has_add_permission(self, request: HttpRequest) -> bool:
#         return False

#     def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
#         if request.user.has_perm("inventory.change_product"):
#             return True
#         else:
#             return False

#     def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
#         return False

#     def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
#         """user can view content from 9:00 to 17:00"""
#         time_now = timezone.now()
#         if time_now.hour >= 9 and time_now.hour <= 17:
#             return True
#         return False


@admin.register(Product)
class ProductAdmin(GuardedModelAdmin):
    list_display = ("name", "web_id", "slug", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("web_id",)}

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        data = self.get_model_objects(request)
        return data

    def has_module_permission(self, request: HttpRequest) -> bool:
        if super().has_module_permission(request):
            return True
        return self.get_model_objects(request).exists()

    def get_model_objects(self, request, action=None, klass=None):
        """
        This function returns a list of items based on the object
        permissions for a particular user.
        """
        opts = self.opts
        actions = [action] if action else ["view", "edit", "delete"]
        klass = klass if klass else opts.model
        model_name = klass._meta.model_name
        return get_objects_for_user(
            user=request.user, perms=[f"{perm}_{model_name}" for perm in actions], klass=klass, any_perm=True
        )

    def has_permission(self, request: HttpRequest, obj, action) -> bool:
        opts = self.opts
        code_name = f"{action}_{opts.model_name}"

        if obj:
            return request.user.has_perm(f"{opts.app_label}.{code_name}", obj)
        else:
            return self.get_model_objects(request).exists()

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return self.has_permission(request, obj, "view")

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return self.has_permission(request, obj, "change")

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return self.has_permission(request, obj, "delete")

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    search_fields = ("email", "username", "first_name", "last_name", "middle_name")
    list_display = ("email", "username", "first_name", "last_name", "middle_name", "is_active", "is_staff")
    ordering = ("-date_joined",)
    list_filter = ("is_staff", "is_superuser", "is_active")
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "middle_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Important dates", {"fields": ("last_login",)}),
        ("Groups", {"fields": ("groups",)}),
        ("User Permissions", {"fields": ("user_permissions",)}),

    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "middle_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

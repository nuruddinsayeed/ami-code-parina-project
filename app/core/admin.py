from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User


class UserAdmin(BaseUserAdmin):
    """Customizing user admin to support our custom user model"""

    ordering = ["id", ]
    list_display = ["email", "name", ]


admin.site.register(User, UserAdmin)

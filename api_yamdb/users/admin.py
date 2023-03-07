from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'role', 'is_staff', 'is_superuser')


admin.site.register(User, CustomUserAdmin)

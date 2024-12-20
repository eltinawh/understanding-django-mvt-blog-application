# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        "email",
        "bio",  
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("bio",)}),)
    add_fieldsets = ((None, {"fields": ("username", "email", "bio",)}),)
    
admin.site.register(CustomUser, CustomUserAdmin)
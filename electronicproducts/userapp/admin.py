"""from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from ajax_select import make_ajax_form
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['full_name', 'password']
    search_fields = ['full_name']

class CustomTokenAdmin(TokenAdmin):
    form = make_ajax_form(Token, {
        'user': 'users'
    })
    search_fields = ["user__full_name"]

admin.site.register(User, UserAdmin)
admin.site.unregister(Token)
admin.site.register(Token, CustomTokenAdmin)"""


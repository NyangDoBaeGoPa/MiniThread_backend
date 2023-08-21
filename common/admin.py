from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from common.models import User


class UserAdmin(UserAdmin):
    list_display = ('account_id', 'user_name', 'date_joined')
    ordering = ()
    list_filter = ()


# Register your models here.
admin.site.register(User, UserAdmin)

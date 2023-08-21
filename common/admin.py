from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from common.models import User


class UserAdmin(UserAdmin):
    list_display = ('username', 'date_joined')


# Register your models here.
admin.site.register(User, UserAdmin)

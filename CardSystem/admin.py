from django.contrib import admin
# Register your models here.
from .models import Cards, Users


class PostAdminCards(admin.ModelAdmin):
    list_display = ['username', 'title', 'name', 'phone', 'address', 'email', 'wechat', 'qq', 'time']


class PostAdminUsers(admin.ModelAdmin):
    list_display = ['username',  'create_time']

admin.site.register(Cards, PostAdminCards)
admin.site.register(Users, PostAdminUsers)

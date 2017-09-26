from django.contrib import admin
# Register your models here.
from .models import Cards, Users


class PostAdminCards(admin.ModelAdmin):
    list_display = ['id', 'username', 'title', 'name', 'phone', 'address', 'email', 'wechat', 'qq', 'time',
                    'image0', 'image1', 'image2', 'image3', 'image4', 'background']


class PostAdminUsers(admin.ModelAdmin):
    list_display = ['id', 'username',  'create_time']

admin.site.register(Cards, PostAdminCards)
admin.site.register(Users, PostAdminUsers)

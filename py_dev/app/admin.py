from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    list_display_links = ('id', 'name', 'age')


admin.site.register(Users, UsersAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Category, CategoryAdmin)


class RaitingAdmin(admin.ModelAdmin):
    list_display = ('star',)
    list_display_links = ('star',)


admin.site.register(Raiting, RaitingAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('them', 'text', 'user')
    list_display_links = ('them', 'text',)


admin.site.register(Comments, CommentsAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'discription', 'comments', 'category')
    list_display_links = ('name', 'quantity', 'discription',)


admin.site.register(Item, ItemAdmin)


class SalesmansAdmin(admin.ModelAdmin):
    list_display = ('name', 'discription', 'comments',)
    list_display_links = ('name', 'discription',)


admin.site.register(Salesmans, SalesmansAdmin)


class BasketAdmin(admin.ModelAdmin):
    list_display = ('cost',)
    list_display_links = ('cost',)


admin.site.register(Basket, BasketAdmin)
# Register your models here.

from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    list_display_links = ('name',)


admin.site.register(Users, UsersAdmin)

# Register your models here.

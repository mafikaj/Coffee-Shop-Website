# lunalatte/admin.py
from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')


admin.site.register(MenuItem, MenuItemAdmin)

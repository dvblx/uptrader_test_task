from django.contrib import admin
from .models import *


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['mi_name', 'slug', 'mi_parent']
    prepopulated_fields = {"slug": ("mi_name", )}


class MenuAdmin(admin.ModelAdmin):
    list_display = ['menu_name', 'slug']
    prepopulated_fields = {"slug": ("menu_name",)}


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)

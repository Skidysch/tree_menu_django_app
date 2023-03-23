from django.contrib import admin
from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'url', 'menu', 'parent')
    list_filter = ('menu',)
    search_fields = ('name', 'url')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)

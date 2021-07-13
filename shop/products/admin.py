from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category']
    list_display_links = ['name', 'description']
    search_fields = ['name']

admin.site.register(Product,ProductAdmin)

admin.site.register(Category)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','user', 'status', 'date']
    readonly_fields = ['date']

admin.site.register(Order,OrderAdmin)


from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category']
    list_display_links = ['name', 'description']
    search_fields = ['name']

admin.site.register(Product,ProductAdmin)

admin.site.register(Category)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','user', 'status', 'date', 'total']
    readonly_fields = ['date', 'date_updated']

admin.site.register(Order,OrderAdmin)
admin.site.register(Promo)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'text', 'date_created']
    readonly_fields = ['user', 'product', 'text', 'date_created']
admin.site.register(Review,ReviewAdmin)
adadmin.site.register(UserCode)


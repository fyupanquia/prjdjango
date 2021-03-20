from django.contrib import admin

# Register your models here.
from orders.models import Client, Article, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    search_fields=('name', 'address')

class ArticleAdmin(admin.ModelAdmin):
    list_filter = ('section',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'delivered')
    list_filter = ('date',)
    date_hierarchy='date'

admin.site.register(Client, ClientAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Order, OrderAdmin)

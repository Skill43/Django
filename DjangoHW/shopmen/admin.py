from django.contrib import admin

from .models import Client, Product, Order

@admin.action(description='обнулить сумму')
def admintest(modeladmin, request, queryset):
    queryset.update(summa=0)
class AdminClient(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    list_filter = ('name',)
    search_fields = ('name',)
    # fields = ('name', 'email', 'phone', 'address')
    # readonly_fields = ('email', 'phone', 'address')
    fieldsets = [['Личный данные', {'fields': ['name', 'email', 'phone', 'address']}]]

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'cnt', 'dataapp')
    list_filter = ('name',)
    # fields = ('name', 'description', 'price', 'cnt', 'dataapp')
    # readonly_fields = ('name', 'description', 'price', 'cnt', 'dataapp')
    fieldsets = [['Данные о товаре', {'fields': ['name', 'description', 'price', 'cnt']}]]


class AdminOrder(admin.ModelAdmin):
    list_display = ('summa', 'dataapp', 'customer')
    list_filter = ('summa',)
    # fields = ('summa', 'dataapp', 'customer')
    # readonly_fields = ('summa', 'dataapp', 'customer')
    fieldsets = [['Цена', {'fields': ['summa']}]]
    actions = [admintest]

admin.site.register(Client, AdminClient)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
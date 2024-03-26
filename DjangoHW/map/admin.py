from django.contrib import admin

# Register your models here.

from .models import Client
@admin.action(description='Тестовый вариант')
def admintest(modeladmin, request, queryset):
    queryset.update(name='test')
class AdminClient(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address')
    list_filter = ('name',)
    search_fields = ('name', 'email')
    # fields = ('name', 'email', 'phone', 'address')
    # readonly_fields = ('email', 'phone', 'address')
    fieldsets = [['ФИО', {'fields': ['name', 'email']}], ['телефон', {'fields': ['phone']}]]
    actions = [admintest]
admin.site.register(Client, AdminClient)

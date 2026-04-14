from django.contrib import admin
from .models import Employee, Product, Order, Profile

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'total_display', 'created_at', 'is_deleted')
    list_filter = ('is_deleted', 'created_at') # Filtro avançado lateral

    def total_display(self, obj):
        return f"R$ {obj.total_value()}"
    total_display.short_description = 'Valor Total'

admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Profile)
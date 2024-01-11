from django.contrib import admin
from .models import category,Product,Order
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":('name',)}
admin.site.register(category,categoryAdmin)

class productAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":('product_name',)}
admin.site.register(Product,productAdmin)

admin.site.register(Order)
# admin.site.register(OrderedItems)

from django.contrib import admin
from core.models import  Category, Vendor, Address


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']

class AddressAdmin(admin.ModelAdmin):
    list_editable = ['address', 'status']
    list_display = ['user', 'address', 'status']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Address, AddressAdmin)

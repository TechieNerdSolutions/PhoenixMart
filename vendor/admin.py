from django.contrib import admin
from .models import Vendor

from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'contact_emergency', 'is_registered')
    list_filter = ('is_registered',)
    search_fields = ('user__username', 'title')
    readonly_fields = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'image', 'cover_image', 'description', 'address', 'contact_emergency', 'chat_resp_time', 'shipping_on_time', 'authentic_rating', 'days_return', 'warranty_period', 'website_url', 'social_media_handles')
        }),
        ('Permissions', {
            'fields': ('is_registered', 'is_verified')
        }),
    )
    ordering = ('user',)
    filter_horizontal = ()


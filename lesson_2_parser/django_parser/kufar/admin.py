from django.contrib import admin
from .models import Furniture


class FurnitureAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'price', 'parse_datetime']
    list_display_links = ['description']
    search_fields = ['id', 'description', 'price', 'parse_datetime']
    # list_editable = ['description', 'price', 'parse_datetime']
    list_filter = ['price', 'parse_datetime']

admin.site.register(Furniture,  FurnitureAdmin)

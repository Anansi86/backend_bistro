from django.contrib import admin
from .models import menu_item

class menu_itemAdmin(admin.ModelAdmin):
    pass
admin.site.register(menu_item, menu_itemAdmin)
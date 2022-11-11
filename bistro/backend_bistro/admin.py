from django.contrib import admin
from .models import menu_item, category, cuisine


class menu_itemAdmin(admin.ModelAdmin):
    pass
admin.site.register(menu_item, menu_itemAdmin)

class categoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(category, categoryAdmin)

class cuisineAdmin(admin.ModelAdmin):
    pass
admin.site.register(cuisine, cuisineAdmin)
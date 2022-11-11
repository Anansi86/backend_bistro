from django.contrib import admin
from .models import menu_item, Category, Cuisine


class menu_itemAdmin(admin.ModelAdmin):
    pass
admin.site.register(menu_item, menu_itemAdmin)

class categoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, categoryAdmin)

class cuisineAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cuisine, cuisineAdmin)
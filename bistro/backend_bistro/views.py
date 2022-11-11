from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

def index(request):

    menuItems = menu_item.objects.all()

    data = [] #we make an empty array to populate a list into

    for menu in menuItems:
        cuisine = Cuisine.objects.get(id=menu.cuisine_id)
        category = Category.objects.get(id=menu.category_id)
        menu_dict = {
            "title": menu.title,
            "price": menu.price,
            "cuisine": {
                "id": cuisine.id,
                "title": cuisine.title,
            },
            "category": category.title,
            "spicey_level": menu.spicey_level,
        }
        data.append(menu_dict)

    return JsonResponse(data, safe=False)
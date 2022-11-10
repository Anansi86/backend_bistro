from django.shortcuts import render
from django.http import HttpResponse
from .models import menu_item

# Create your views here.



def index(request):
    menu = list(menu_item.objects.values())
    print(menu)
    return JsonResponse({ 'data': menu }) 

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(request):
    menu  = list(menu_item.objects.values())
    print(Menu)
    return JsonResponse({ 'data': menu }) 

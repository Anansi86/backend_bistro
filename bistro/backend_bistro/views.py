from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer
#from django.http import HttpResponse, JsonResponse




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

#def index(request):

 #   menuItems = menu_item.objects.all()

#    data = [] #we make an empty array to populate a list into
#
#    for menu in menuItems:
#        cuisine = Cuisine.objects.get(id=menu.cuisine_id)
#        category = Category.objects.get(id=menu.category_id)
#        menu_dict = {
#            "title": menu.title,
#            "id": menu.id,
#            "price": menu.price,
#            "cuisine": {
#                "id": cuisine.id,
#                "title": cuisine.title,
#            },
#            "category": category.title,
#            "spicey_level": menu.spicey_level,
#            "description": menu.description,
#        }
#        data.append(menu_dict)
#
#    return JsonResponse(data, safe=False)
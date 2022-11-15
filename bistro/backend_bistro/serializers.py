from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers):
    class Meta:
        model = User
        fields = ['url',]


#class GroupSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Group
#        fields = ['url', 'name']
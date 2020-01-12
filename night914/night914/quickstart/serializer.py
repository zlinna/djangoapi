from django.contrib.auth.models import User, Group
from rest_framework import serializers

# 使用的超链接关系HyperlinkedModelSerializer。您也可以使用主键和各种其他关系，但是超链接是一种很好的RESTful设计。
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

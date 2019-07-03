from rest_framework import serializers
from shop.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('name', 'price', 'image', 'category')

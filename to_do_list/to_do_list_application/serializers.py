from rest_framework import serializers
from .models import To_do_item

class To_do_itemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = To_do_item
        fields = ('id', 'url', 'name', 'course', 'deadline', 'soort')

from rest_framework import serializers
from .models import To_do_item

class To_do_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = To_do_item
        fields = ('id','name', 'course', 'soort')

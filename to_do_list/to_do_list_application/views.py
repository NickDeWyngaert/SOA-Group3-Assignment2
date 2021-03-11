from django.shortcuts import render
from rest_framework import viewsets
from .models import To_do_item
from .serializers import To_do_itemSerializer


class To_do_itemView(viewsets.ModelViewSet):
    queryset = To_do_item.objects.all()
    serializer_class = To_do_itemSerializer

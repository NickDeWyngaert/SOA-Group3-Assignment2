from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('to_do_items', views.To_do_itemView)

urlpatterns = [
    path('', include(router.urls))    
]

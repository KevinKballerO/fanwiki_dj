from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'character', views.CharacterViewSet)
router.register(r'episodes', views.EpisodesViewSet)

urlpatterns = [
    #path('api/', include(router.urls))
    path('', include(router.urls))
]
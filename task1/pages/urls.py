from django.urls import path, include
from rest_framework import routers
from . import views

from .views import Music

router = routers.DefaultRouter()
router.register('music',views.MusicView)

urlpatterns = [
    path('', Music.as_view(), name='music'),
    path('api/', include(router.urls)),
]




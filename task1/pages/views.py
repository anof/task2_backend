# REST WORK

from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Music
from .serializers import MusicSerializer


class MusicView(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class Music(TemplateView):
    template_name = 'music.html'
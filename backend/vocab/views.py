from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MicroblogSerializer, VocabItemSerializer, VocabListSerializer
from .models import Microblog, VocabItem, VocabList
# Create your views here.


class MicroblogView(viewsets.ModelViewSet):
    serializer_class = MicroblogSerializer
    queryset = Microblog.objects.all()


class VocabItemView(viewsets.ModelViewSet):
    serializer_class = VocabItemSerializer
    queryset = VocabItem.objects.all()


class VocabListView(viewsets.ModelViewSet):
    serializer_class = VocabListSerializer
    queryset = VocabList.objects.all()


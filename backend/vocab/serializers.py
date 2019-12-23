from rest_framework import serializers
from .models import VocabItem, VocabList, Microblog


class VocabItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabItem
        fields = ('id', 'text', 'meaning', 'language', 'morphology', 'pronunciation', 'category', 'subcategory', 'source', 'last_practiced')


class VocabListSerializer(serializers.ModelSerializer):
    model = VocabList
    fields = ('id', 'learner')


class MicroblogSerializer(serializers.ModelSerializer):
    model = Microblog
    fields = ('id', 'text', 'language', 'learner')


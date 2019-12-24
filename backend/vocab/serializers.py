from rest_framework import serializers
from .models import VocabItem, VocabList, Microblog


class VocabItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabItem
        fields = ('id', 'text', 'meaning', 'language', 'morphology', 'pronunciation', 'category', 'subcategory', 'source', 'last_practiced')


class VocabListSerializer(serializers.ModelSerializer):
    vocab_items = VocabItemSerializer(many=True)
    class Meta:
        model = VocabList
        fields = ('id', 'learner', 'vocab_items')


class MicroblogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microblog
        fields = ('id', 'text', 'language', 'learner')


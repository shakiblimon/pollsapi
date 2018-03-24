from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, serializers
from.import models
from .import serializers


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerilizer
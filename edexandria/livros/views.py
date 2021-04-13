from django.shortcuts import render
from rest_framework import viewsets
from edexandria.livros.models import Livro
from edexandria.livros.serializers import LivroSerializer

# Create your views here.

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
from edexandria.livros.models import Livro
from rest_framework import serializers

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['titulo', 'isbn', 'ano', 'edicao', 'paginas']
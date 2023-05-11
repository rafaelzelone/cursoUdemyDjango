from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kargs = {
            'email': { 'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'avaliacao',
            'atualizacao',
            'publicacao', 
            'ativo',
        )
    def validate_avaliacao(self, valor):
        if valor in range(0, 6):
            return valor
        raise serializers.ValidationError('A avaliação dev conter numero entre 0 e 5')


class CursoSerializer(serializers.ModelSerializer):
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True, 
    #     read_only=True, 
    #     view_name='avaliacao-detail')
    avaliacoes = serializers.PrimaryKeyRelatedField(
        many=True, 
        read_only=True, 
       )
    
    media_avaliacoes = serializers.SerializerMethodField()
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'atualizacao',
            'publicacao', 
            'ativo',
            'avaliacoes',
            "media_avaliacoes"
        )
    

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return round(media * 2) / 2

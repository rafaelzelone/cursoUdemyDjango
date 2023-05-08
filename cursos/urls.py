from django.urls import path
from .views import CursoApiView, AvaliacaoApiView, AvaliacoesApiView, CursosApiView


urlpatterns = [
    path('cursos/', CursosApiView.as_view(), name="cursos"),
    path('cursos/<int:pk>/', CursoApiView.as_view(), name="curso"),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesApiView.as_view(), name="avaliacoes_curso"),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoApiView.as_view(), name="curso_avaliacao"),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name="avaliacoes"),
    path('avaliacao/<int:avaliacao_pk>/', AvaliacaoApiView.as_view(), name="avaliacao"),
]
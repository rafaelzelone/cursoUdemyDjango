from django.urls import path
from .views import CursoApiView, AvaliacaoApiView, AvaliacoesApiView, CursosApiView


urlpatterns = [
    path('cursos/', CursosApiView.as_view(), name="cursos"),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name="avaliacoes"),
    path('cursos/<int:pk>/', CursoApiView.as_view(), name="curso"),
    path('avaliacao/<int:pk>/', AvaliacaoApiView.as_view(), name="avaliacao"),
]
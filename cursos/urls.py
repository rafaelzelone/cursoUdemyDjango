from django.urls import path
from .views import CursoApiView, AvaliacaoApiView, AvaliacoesApiView, CursosApiView, CursoViewSet, AvaliacaoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('curso', CursoViewSet)
router.register('avaliacao', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosApiView.as_view(), name="cursos"),
    path('cursos/<int:pk>/', CursoApiView.as_view(), name="curso"),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesApiView.as_view(), name="avaliacoes_curso"),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoApiView.as_view(), name="curso_avaliacao"),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name="avaliacoes"),
    path('avaliacao/<int:avaliacao_pk>/', AvaliacaoApiView.as_view(), name="avaliacao"),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AdministradoresViewSet, CandidatosViewSet, CurriculumViewSet, DepartamentosViewSet,
    EmpleosViewSet, EmpresasViewSet, MunicipiosViewSet, PostulacionesViewSet, VacantesViewSet
)

#crea las direcciones de las url de cada tabla
router = DefaultRouter()
router.register(r'administradores', AdministradoresViewSet)
router.register(r'candidatos', CandidatosViewSet)
router.register(r'curriculum', CurriculumViewSet)
router.register(r'departamentos', DepartamentosViewSet)
router.register(r'empleos', EmpleosViewSet)
router.register(r'empresas', EmpresasViewSet)
router.register(r'municipios', MunicipiosViewSet)
router.register(r'postulaciones', PostulacionesViewSet)
router.register(r'vacantes', VacantesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from .views import home

urlpatterns += [
    path('', home),
]

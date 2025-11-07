from rest_framework import viewsets
from .models import (
    Administradores, Candidatos, Curriculum, Departamentos, Empleos,
    Empresas, Municipios, Postulaciones, Vacantes
)
from .serializers import (
    AdministradoresSerializer, CandidatosSerializer, CurriculumSerializer, DepartamentosSerializer,
    EmpleosSerializer, EmpresasSerializer, MunicipiosSerializer, PostulacionesSerializer, VacantesSerializer
)

class AdministradoresViewSet(viewsets.ModelViewSet):
    queryset = Administradores.objects.all()
    serializer_class = AdministradoresSerializer

class CandidatosViewSet(viewsets.ModelViewSet):
    queryset = Candidatos.objects.all()
    serializer_class = CandidatosSerializer

class CurriculumViewSet(viewsets.ModelViewSet):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer

class DepartamentosViewSet(viewsets.ModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer

class EmpleosViewSet(viewsets.ModelViewSet):
    queryset = Empleos.objects.all()
    serializer_class = EmpleosSerializer


class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer

class MunicipiosViewSet(viewsets.ModelViewSet):
    queryset = Municipios.objects.all()
    serializer_class = MunicipiosSerializer

class PostulacionesViewSet(viewsets.ModelViewSet):
    queryset = Postulaciones.objects.all()
    serializer_class = PostulacionesSerializer

class VacantesViewSet(viewsets.ModelViewSet):
    queryset = Vacantes.objects.all()
    serializer_class = VacantesSerializer



from django.http import JsonResponse

def home(request):
    return JsonResponse({"mensaje": "Bienvenido a la API de ImpulsoNica"})

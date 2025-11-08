from rest_framework import serializers
from .models import (
    Administradores, Candidatos, Curriculum, Departamentos, Empleos,
    Empresas, Municipios, Postulaciones, Vacantes
)
# la serealizacion de la aca tabla de la base de datos
class AdministradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administradores
        fields = '__all__'

class CandidatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatos
        fields = '__all__'

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'

class EmpleosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleos
        fields = '__all__'

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'

class MunicipiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = '__all__'

class PostulacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulaciones
        fields = '__all__'

class VacantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacantes
        fields = '__all__'

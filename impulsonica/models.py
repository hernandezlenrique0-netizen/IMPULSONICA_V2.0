# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

#modelado de la tablas de la base de datos
from django.db import models

class Administradores(models.Model):
    administradorid = models.AutoField(db_column='AdministradorId', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', unique=True, max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    municipioid = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='MunicipioId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Administradores'


class Candidatos(models.Model):
    candidatoid = models.AutoField(db_column='CandidatoId', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    estadocivil = models.CharField(db_column='EstadoCivil', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    curriculumid = models.ForeignKey('Curriculum', models.DO_NOTHING, db_column='CurriculumId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Candidatos'


class Curriculum(models.Model):
    curriculumid = models.AutoField(db_column='CurriculumId', primary_key=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechanacimiento = models.DateField(db_column='FechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='Nacionalidad', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    niveleducativo = models.CharField(db_column='NivelEducativo', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    profesion = models.CharField(db_column='Profesion', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    experiencialaboral = models.CharField(db_column='ExperienciaLaboral', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    habilidades = models.CharField(db_column='Habilidades', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idiomas = models.CharField(db_column='Idiomas', max_length=150, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    referencias = models.CharField(db_column='Referencias', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curriculum'


class Departamentos(models.Model):
    departamentoid = models.AutoField(db_column='DepartamentoId', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departamentos'


class Empleos(models.Model):
    empleoid = models.AutoField(db_column='EmpleoId', primary_key=True)  # Field name made lowercase.
    nombreempleo = models.CharField(db_column='NombreEmpleo', max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    requisitos = models.CharField(db_column='Requisitos', max_length=500, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    salario = models.DecimalField(db_column='Salario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tipoempleo = models.CharField(db_column='TipoEmpleo', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    modalidad = models.CharField(db_column='Modalidad', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechapublicacion = models.DateTimeField(db_column='FechaPublicacion', blank=True, null=True)  # Field name made lowercase.
    fechacierre = models.DateTimeField(db_column='FechaCierre', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    empresaid = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='EmpresaId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleos'


class Empresas(models.Model):
    empresaid = models.AutoField(db_column='EmpresaId', primary_key=True)  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='NombreEmpresa', max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='Sector', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipoempresa = models.CharField(db_column='TipoEmpresa', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecharegistro = models.DateTimeField(db_column='FechaRegistro', blank=True, null=True)  # Field name made lowercase.
    municipioid = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='MunicipioId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empresas'


class Municipios(models.Model):
    municipioid = models.AutoField(db_column='MunicipioId', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    departamentoid = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='DepartamentoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Municipios'


class Postulaciones(models.Model):
    postulacionid = models.AutoField(db_column='PostulacionId', primary_key=True)  # Field name made lowercase.
    fechapostulacion = models.DateTimeField(db_column='FechaPostulacion', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    candidatoid = models.ForeignKey(Candidatos, models.DO_NOTHING, db_column='CandidatoId')  # Field name made lowercase.
    empleoid = models.ForeignKey(Empleos, models.DO_NOTHING, db_column='EmpleoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Postulaciones'


class Vacantes(models.Model):
    vacanteid = models.AutoField(db_column='VacanteId', primary_key=True)  # Field name made lowercase.
    empleoid = models.ForeignKey(Empleos, models.DO_NOTHING, db_column='EmpleoId')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='FechaFin', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=500, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vacantes'

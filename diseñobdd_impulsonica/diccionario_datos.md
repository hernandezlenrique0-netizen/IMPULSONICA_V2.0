# Diccionario de Datos – ImpulsoNica

Este documento describe las tablas y campos utilizados en la base de datos del sistema ImpulsoNica.

---

## Tabla: Departamentos

| Campo           | Tipo de dato | Restricciones        | Descripción                          |
|----------------|--------------|----------------------|--------------------------------------|
| DepartamentoId | INT          | PK, IDENTITY(1,1)    | Identificador único del departamento |
| Nombre         | VARCHAR(100) | NOT NULL             | Nombre del departamento              |

---

## Tabla: Municipios

| Campo           | Tipo de dato | Restricciones        | Descripción                          |
|----------------|--------------|----------------------|--------------------------------------|
| MunicipioId    | INT          | PK, IDENTITY(1,1)    | Identificador único del municipio    |
| Nombre         | VARCHAR(100) | NOT NULL             | Nombre del municipio                 |
| DepartamentoId | INT          | FK → Departamentos   | Relación con el departamento         |

---

## Tabla: Administradores

| Campo         | Tipo de dato   | Restricciones        | Descripción                          |
|--------------|----------------|----------------------|--------------------------------------|
| AdministradorId | INT         | PK, IDENTITY(1,1)    | Identificador del administrador      |
| Nombre        | VARCHAR(100)  | NOT NULL             | Nombre del administrador             |
| Apellido      | VARCHAR(100)  | NOT NULL             | Apellido del administrador           |
| Correo        | VARCHAR(150)  | UNIQUE, NOT NULL     | Correo electrónico                   |
| Telefono      | VARCHAR(20)   | NULL                 | Número de teléfono                   |
| Usuario       | VARCHAR(50)   | UNIQUE, NOT NULL     | Nombre de usuario                    |
| Contrasena    | VARCHAR(255)  | NOT NULL             | Contraseña (se recomienda hash)      |
| FechaRegistro | DATETIME      | DEFAULT GETDATE()    | Fecha de registro                    |
| MunicipioId   | INT           | FK → Municipios      | Relación con municipio               |

---

## Tabla: Empresas

| Campo         | Tipo de dato   | Restricciones        | Descripción                          |
|--------------|----------------|----------------------|--------------------------------------|
| EmpresaId     | INT           | PK, IDENTITY(1,1)    | Identificador de la empresa          |
| NombreEmpresa | VARCHAR(150)  | NOT NULL             | Nombre comercial                     |
| Correo        | VARCHAR(150)  | UNIQUE, NOT NULL     | Correo electrónico                   |
| Telefono      | VARCHAR(20)   | NULL                 | Número de contacto                   |
| Direccion     | VARCHAR(255)  | NULL                 | Dirección física                     |
| Sector        | VARCHAR(100)  | NULL                 | Sector económico                     |
| TipoEmpresa   | VARCHAR(100)  | NULL                 | Privada, Pública, ONG, etc.          |
| FechaRegistro | DATETIME      | DEFAULT GETDATE()    | Fecha de registro                    |
| MunicipioId   | INT           | FK → Municipios      | Ubicación de la empresa              |

---

## Tabla: Curriculum

| Campo             | Tipo de dato   | Restricciones        | Descripción                          |
|------------------|----------------|----------------------|--------------------------------------|
| CurriculumId      | INT           | PK, IDENTITY(1,1)    | Identificador del currículum         |
| NombreCompleto    | VARCHAR(150)  | NOT NULL             | Nombre completo del candidato        |
| Correo            | VARCHAR(150)  | NOT NULL             | Correo electrónico                   |
| Telefono          | VARCHAR(20)   | NULL                 | Número de contacto                   |
| Direccion         | VARCHAR(255)  | NULL                 | Dirección física                     |
| FechaNacimiento   | DATE          | NULL                 | Fecha de nacimiento                  |
| Nacionalidad      | VARCHAR(100)  | NULL                 | Nacionalidad                         |
| NivelEducativo    | VARCHAR(100)  | NULL                 | Nivel académico                      |
| Profesion         | VARCHAR(100)  | NULL                 | Profesión principal                  |
| ExperienciaLaboral| VARCHAR(255)  | NULL                 | Breve resumen de experiencia         |
| Habilidades       | VARCHAR(255)  | NULL                 | Habilidades técnicas o blandas       |
| Idiomas           | VARCHAR(150)  | NULL                 | Idiomas hablados                     |
| Referencias       | VARCHAR(255)  | NULL                 | Referencias laborales                |
| FechaRegistro     | DATETIME      | DEFAULT GETDATE()    | Fecha de registro                    |

---

## Tabla: Candidatos

| Campo         | Tipo de dato   | Restricciones        | Descripción                          |
|--------------|----------------|----------------------|--------------------------------------|
| CandidatoId   | INT           | PK, IDENTITY(1,1)    | Identificador del candidato          |
| Nombre        | VARCHAR(100)  | NOT NULL             | Nombre del candidato                 |
| Apellido      | VARCHAR(100)  | NOT NULL             | Apellido del candidato               |
| Correo        | VARCHAR(150)  | UNIQUE, NOT NULL     | Correo electrónico                   |
| Telefono      | VARCHAR(20)   | NULL                 | Número de contacto                   |
| Direccion     | VARCHAR(255)  | NULL                 | Dirección física                     |
| Genero        | VARCHAR(20)   | NULL                 | Género                               |
| FechaNacimiento| DATE         | NULL                 | Fecha de nacimiento                  |
| EstadoCivil   | VARCHAR(50)   | NULL                 | Estado civil                         |
| Nacionalidad  | VARCHAR(100)  | NULL                 | Nacionalidad                         |
| FechaRegistro | DATETIME      | DEFAULT GETDATE()    | Fecha de registro                    |
| CurriculumId  | INT           | FK → Curriculum      | Relación con currículum              |

---
## Tabla: Empleos

| Campo         | Tipo de dato   | Restricciones        | Descripción                                 |
|--------------|----------------|----------------------|---------------------------------------------|
| EmpleoId      | INT           | PK, IDENTITY(1,1)    | Identificador del empleo                    |
| NombreEmpleo  | VARCHAR(150)  | NOT NULL             | Título del puesto                           |
| Descripcion   | TEXT          | NULL                 | Descripción general del empleo              |
| Requisitos    | TEXT          | NULL                 | Requisitos solicitados                      |
| Salario       | DECIMAL(10,2) | NULL                 | Salario ofrecido                            |
| TipoEmpleo    | VARCHAR(100)  | NULL                 | Tiempo completo, medio tiempo, etc.         |
| Modalidad     | VARCHAR(50)   | NULL                 | Presencial, remoto, híbrido                 |
| FechaCierre   | DATE          | NULL                 | Fecha límite para aplicar                   |
| Estado        | VARCHAR(50)   | DEFAULT 'Activo'     | Estado del empleo (Activo/Inactivo)         |
| EmpresaId     | INT           | FK → Empresas        | Empresa que publica el empleo               |

---

## Tabla: Postulaciones

| Campo           | Tipo de dato   | Restricciones        | Descripción                                         |
|----------------|----------------|----------------------|-----------------------------------------------------|
| PostulacionId   | INT           | PK, IDENTITY(1,1)    | Identificador de la postulación                     |
| FechaPostulacion| DATETIME      | NOT NULL             | Fecha y hora en que se realizó la postulación       |
| Estado          | VARCHAR(50)   | DEFAULT 'Pendiente'  | Estado de la postulación (Pendiente, Aprobada, Rechazada) |
| CandidatoId     | INT           | FK → Candidatos      | Candidato que aplica                                |
| EmpleoId        | INT           | FK → Empleos         | Empleo al que se aplica                             |

---

## Tabla: Vacantes

| Campo         | Tipo de dato   | Restricciones        | Descripción                                 |
|--------------|----------------|----------------------|---------------------------------------------|
| VacanteId     | INT           | PK, IDENTITY(1,1)    | Identificador de la vacante                 |
| EmpleoId      | INT           | FK → Empleos         | Empleo asociado a la vacante                |
| Cantidad      | INT           | NOT NULL             | Número de plazas disponibles                |
| FechaInicio   | DATE          | NOT NULL             | Fecha de inicio de publicación              |
| FechaFin      | DATE          | NOT NULL             | Fecha de cierre de la vacante               |
| Estado        | VARCHAR(50)   | DEFAULT 'Activa'     | Estado de la vacante                        |
| Observaciones | TEXT          | NULL                 | Comentarios adicionales sobre la vacante    |

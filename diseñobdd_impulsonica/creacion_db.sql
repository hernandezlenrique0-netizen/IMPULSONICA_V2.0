-- Crear base de datos
CREATE DATABASE ImpulsoNica;
GO

USE ImpulsoNica;
GO

-- Tabla: Departamentos
CREATE TABLE Departamentos (
    DepartamentoId INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL
);

-- Tabla: Municipios
CREATE TABLE Municipios (
    MunicipioId INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL,
    DepartamentoId INT NOT NULL,
    FOREIGN KEY (DepartamentoId) REFERENCES Departamentos(DepartamentoId)
);

-- Tabla: Administradores
CREATE TABLE Administradores (
    AdministradorId INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Correo VARCHAR(150) UNIQUE NOT NULL,
    Telefono VARCHAR(20),
    Usuario VARCHAR(50) UNIQUE NOT NULL,
    Contrasena VARCHAR(255) NOT NULL, -- En producción se recomienda guardar en hash
    FechaRegistro DATETIME DEFAULT GETDATE(),
    MunicipioId INT NOT NULL,
    FOREIGN KEY (MunicipioId) REFERENCES Municipios(MunicipioId)
);

-- Tabla: Empresas
CREATE TABLE Empresas (
    EmpresaId INT PRIMARY KEY IDENTITY(1,1),
    NombreEmpresa VARCHAR(150) NOT NULL,
    Correo VARCHAR(150) UNIQUE NOT NULL,
    Telefono VARCHAR(20),
    Direccion VARCHAR(255),
    Sector VARCHAR(100),              -- Ejemplo: Tecnología, Educación, Salud
    TipoEmpresa VARCHAR(100),         -- Ejemplo: Privada, Pública, ONG
    FechaRegistro DATETIME DEFAULT GETDATE(),
    MunicipioId INT NOT NULL,
    FOREIGN KEY (MunicipioId) REFERENCES Municipios(MunicipioId)
);

-- Tabla: Curriculum
CREATE TABLE Curriculum (
    CurriculumId INT PRIMARY KEY IDENTITY(1,1),
    NombreCompleto VARCHAR(150) NOT NULL,
    Correo VARCHAR(150) NOT NULL,
    Telefono VARCHAR(20),
    Direccion VARCHAR(255),
    FechaNacimiento DATE,
    Nacionalidad VARCHAR(100),
    NivelEducativo VARCHAR(100),       -- Ejemplo: Secundaria, Técnico, Universitario, Posgrado
    Profesion VARCHAR(100),
    ExperienciaLaboral VARCHAR(255),
    Habilidades VARCHAR(255),
    Idiomas VARCHAR(150),
    Referencias VARCHAR(255),
    FechaRegistro DATETIME DEFAULT GETDATE()
);

-- Tabla: Candidatos
CREATE TABLE Candidatos (
    CandidatoId INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    Correo VARCHAR(150) UNIQUE NOT NULL,
    Telefono VARCHAR(20),
    Direccion VARCHAR(255),
    Genero VARCHAR(20),
    FechaNacimiento DATE,
    EstadoCivil VARCHAR(50),
    Nacionalidad VARCHAR(100),
    FechaRegistro DATETIME DEFAULT GETDATE(),
    CurriculumId INT NOT NULL,
    FOREIGN KEY (CurriculumId) REFERENCES Curriculum(CurriculumId)
);

-- Tabla: Empleos
CREATE TABLE Empleos (
    EmpleoId INT PRIMARY KEY IDENTITY(1,1),
    NombreEmpleo VARCHAR(150) NOT NULL,
    Descripcion VARCHAR(500) NOT NULL,
    Requisitos VARCHAR(500),
    Salario DECIMAL(10,2),
    TipoEmpleo VARCHAR(100),             -- Ejemplo: Tiempo completo, Medio tiempo, Práctica
    Modalidad VARCHAR(100),              -- Ejemplo: Presencial, Remoto, Híbrido
    FechaPublicacion DATETIME DEFAULT GETDATE(),
    FechaCierre DATETIME,
    Estado VARCHAR(50) DEFAULT 'Activo',
    EmpresaId INT NOT NULL,
    FOREIGN KEY (EmpresaId) REFERENCES Empresas(EmpresaId)
);

-- Tabla: Postulaciones
CREATE TABLE Postulaciones (
    PostulacionId INT PRIMARY KEY IDENTITY(1,1),
    FechaPostulacion DATETIME DEFAULT GETDATE(),
    Estado VARCHAR(50) DEFAULT 'Pendiente',
    CandidatoId INT NOT NULL,
    EmpleoId INT NOT NULL,
    FOREIGN KEY (CandidatoId) REFERENCES Candidatos(CandidatoId),
    FOREIGN KEY (EmpleoId) REFERENCES Empleos(EmpleoId)
);

-- Tabla: Vacantes
CREATE TABLE Vacantes (
    VacanteId INT PRIMARY KEY IDENTITY(1,1),
    EmpleoId INT NOT NULL,
    Cantidad INT DEFAULT 1,
    FechaInicio DATETIME DEFAULT GETDATE(),
    FechaFin DATETIME,
    Estado VARCHAR(50) DEFAULT 'Activa',
    Observaciones VARCHAR(500),
    FOREIGN KEY (EmpleoId) REFERENCES Empleos(EmpleoId)
);

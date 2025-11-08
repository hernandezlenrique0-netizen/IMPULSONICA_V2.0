## API de Impulsonica

Esta API está diseñada para gestionar la búsqueda de empresas, vacantes y candidatos en un entorno profesional. Desarrollada con Django y Django REST Framework, incluye autenticación JWT, documentación Swagger, y conexión a SQL Server.

## Tecnologías utilizadas

- Python 3.13+
- Django  
- Django REST Framework  
- SQL Server  
- JWT (Json Web Token)  
- Swagger (drf-yasg)  
- Apidog / Postman (para pruebas)

## Instalación

Clona el repositorio:
```bash
https://github.com/hernandezlenrique0-netizen/IMPULSONICA_V2.0.git
cd IMPULSONICA_V2.0
```
# Instala dependencias:
```python
- pip install -r requirements.txt
```

# Configura la base de datos en settings.py
Configuración de base de datos (SQL Server)
un ejemplo para SQL Server usando `pyodbc`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sql_server.pyodbc',
        'NAME': 'NombreBD',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
        },
    }
}
```

# Ejecuta migraciones:
```python
- python manage.py makemigrations
- python manage.py migrate
```
# Inicia el servidor:
```python
- python manage.py runserver
```
# Autenticación
La API utiliza JWT. Para obtener un token:
```python
- POST /api/token/ → Enviar usuario y contraseña
- POST /api/token/refresh/ → Refrescar token
```

Incluye el token en el encabezado:
- Authorization: Bearer <tu_token>

# Accedé a la documentación de la api Swagger en:
http://localhost:8000/swagger/

## Endpoints principales
| Tabla / Recurso     | Ruta base                                           | Métodos disponibles             | Descripción general                          |
|---------------------|-----------------------------------------------------|----------------------------------|----------------------------------------------|
| Administradores     | http://127.0.0.1:8000/api/administradores/          | GET, POST, PUT, DELETE           | Gestión de usuarios administradores          |
| Candidatos          | http://127.0.0.1:8000/api/candidatos/               | GET, POST, PUT, DELETE           | Registro y consulta de candidatos            |
| Curriculum          | http://127.0.0.1:8000/api/curriculum/               | GET, POST, PUT, DELETE           | Información curricular de candidatos         |
| Departamentos       | http://127.0.0.1:8000/api/departamentos/            | GET, POST, PUT, DELETE           | División geográfica por departamentos        |
| Empleos             | http://127.0.0.1:8000/api/empleos/                  | GET, POST, PUT, DELETE           | Tipos de empleo disponibles                  |
| Empresas            | http://127.0.0.1:8000/api/empresas/                 | GET, POST, PUT, DELETE           | Registro y gestión de empresas               |
| Municipios          | http://127.0.0.1:8000/api/municipios/               | GET, POST, PUT, DELETE           | División geográfica por municipios           |
| Postulaciones       | http://127.0.0.1:8000/api/postulaciones/            | GET, POST, PUT, DELETE           | Relación entre candidatos y vacantes         |
| Vacantes            | http://127.0.0.1:8000/api/vacantes/                 | GET, POST, PUT, DELETE           | Ofertas laborales publicadas por empresas    |

# Pruebas
- Apidog
- Postman

## Estructura del proyecto

```plaintext
impulsonica-api/
│
├── impulsonica-api/             # Configuración global del proyecto
│   ├── asgi.py                  # Configuración para despliegue en servidores ASGI
│   ├── settings.py              # Configuración general (BD, apps, middleware, etc.)
│   ├── urls.py                  # Rutas globales del proyecto
│   └── wsgi.py                  # Configuración para despliegue en servidores WSGI
│
├── impulsonica/                 # App principal del sistema
│   ├── __init__.py
│   ├── admin.py                 # Registro de modelos en el panel de administración
│   ├── apps.py                  # Configuración de la app
│   ├── models.py                # Definición de modelos (tablas de BD)
│   ├── views.py                 # Lógica de las vistas (endpoints)
│   ├── serializers.py           # Serialización de modelos a JSON
│   ├── urls.py                  # Rutas específicas de la app
│   └── test.py                  # Pruebas unitarias y funcionales
└── manage.py                    # Script principal para comandos administrativos
```

# Desarrollado por:
Estudiantes de Ingeniería en Sistemas de cuarto semestre de la UNAN-MANAGUA
- Luis Enrique Hernández Lorío
- Irma Mayerling Diaz vargas
- Danilo Antonio Larios Perez
- Dylan Antuan Lopez Lopez

- Email:
-  [hernandezlenrique0@gmail.com]
-  [dylanantuan341@gmail.com]
-  [Danilolarios59@gmail.com]
-  [virma9484@gmail.com]
- GitHub: hernandezlenrique0-netizen

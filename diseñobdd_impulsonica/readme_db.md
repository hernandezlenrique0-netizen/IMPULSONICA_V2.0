# Base de Datos – ImpulsoNica

Este repositorio contiene el diseño y los scripts de la base de datos utilizados en el sistema **ImpulsoNica**, una plataforma de gestión de empleos, candidatos y empresas en Nicaragua.

---

## Estructura del Proyecto
````
diseñobdd_impulsonica/ 
├── creacion_db.sql # Script para crear todas las tablas 
├── diccionario_datos.md # Documento con descripción de todas las tablas
├── diagrama-logico.png # Imagen del diagrama lógico relacional 
````

---

##  Tecnologías

- **SQL Server** (Transact-SQL)
- **Integración con backend Django (proyecto ImpulsoNica)**

---

## scripts disponibles

### 🔹 `creacion_db.sql`

Contiene la definición de todas las tablas del sistema:

- Departamentos
- Municipios
- Administradores
- Empresas
- Currículums
- Candidatos
- Empleos
- Postulaciones
- Vacantes

---

## Cómo usar

1. Abrí SQL Server Management Studio
2. Ejecutá `creacion_db.sql` para crear la estructura 
3. Verificá las relaciones y claves foráneas
5. Integrá con el backend Django usando modelos y migraciones

---

## Recomendaciones

- Validá los tipos de datos y restricciones antes de producción
- Usá `diccionario_datos.md` como referencia para documentación técnica
- Mantené los scripts versionados en Git para trazabilidad

---



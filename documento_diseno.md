# Documento de Diseño – Sistema Básico de Tickets

## 1. Presentación del aplicante

Mi nombre es Sergio Cárdenas. Soy estudiante de Ingeniería de Sistemas y tengo interés en el desarrollo de aplicaciones web, el modelado de datos, la programación backend y el uso de tecnologías como Python, Django y bases de datos relacionales.

## 2. Contexto y objetivo del sistema

El sistema básico de tickets tiene como objetivo permitir que usuarios autenticados puedan registrar solicitudes de soporte, consultar el estado de los tickets que han creado y visualizar la respuesta entregada por un administrador.

Desde el lado administrativo, el sistema permite que un administrador gestione los tickets desde el panel de Django Admin, modifique su estado y registre una respuesta breve para el usuario.

## 3. Alcance de la solución

El sistema incluye las siguientes funcionalidades:

- Inicio de sesión de usuarios mediante el sistema de autenticación de Django.
- Creación de tickets por parte de usuarios autenticados.
- Consulta del listado de tickets creados por el usuario autenticado.
- Consulta del detalle de un ticket propio.
- Gestión de tickets desde Django Admin.
- Cambio de estado del ticket por parte del administrador.
- Registro de una respuesta administrativa para el usuario.

El sistema no incluye:

- Registro público de usuarios.
- Recuperación de contraseña.
- Envío de correos electrónicos.
- Manejo de prioridades.
- Historial detallado de cambios.
- Edición o eliminación de tickets por parte del usuario.
- API REST.

## 4. Historias de usuario

### HU-01 – Inicio de sesión

Como usuario registrado, quiero iniciar sesión en el sistema para poder crear y consultar mis tickets de soporte.

### HU-02 – Crear ticket

Como usuario autenticado, quiero crear un ticket indicando título, descripción y categoría para registrar una solicitud de soporte.

### HU-03 – Consultar mis tickets

Como usuario autenticado, quiero ver únicamente los tickets que he creado para hacer seguimiento a mis solicitudes.

### HU-04 – Ver detalle de ticket

Como usuario autenticado, quiero consultar el detalle de un ticket propio para revisar su descripción, estado y respuesta del administrador.

### HU-05 – Gestionar tickets desde administración

Como administrador, quiero revisar los tickets desde Django Admin, cambiar su estado y registrar una respuesta para informar al usuario sobre la atención de su solicitud.

## 5. Reglas de negocio

| Código | Regla |
|---|---|
| RN-01 | Solo los usuarios autenticados pueden crear tickets. |
| RN-02 | Solo los usuarios autenticados pueden consultar tickets. |
| RN-03 | El estado inicial de todo ticket debe ser “Abierto”. |
| RN-04 | El usuario no puede seleccionar ni modificar el estado del ticket. |
| RN-05 | El usuario solo puede consultar tickets creados por él mismo. |
| RN-06 | Solo el administrador puede cambiar el estado del ticket desde Django Admin. |
| RN-07 | No se permite crear tickets sin título. |
| RN-08 | No se permite crear tickets sin descripción. |
| RN-09 | No se permite crear tickets sin categoría. |

## 6. Decisiones de diseño

Se decidió utilizar el sistema de autenticación nativo de Django para aprovechar un mecanismo ya integrado, probado y adecuado para controlar el acceso de usuarios al sistema.

Se decidió utilizar Django Admin para la gestión administrativa de los tickets, ya que el requerimiento indica que el administrador debe revisar los tickets, cambiar su estado y registrar respuestas desde este panel.

Se decidió crear un modelo `Categoria` separado del modelo `Ticket` para permitir una clasificación ordenada y reutilizable de las solicitudes.

Se decidió manejar el estado del ticket mediante opciones predefinidas para evitar valores inválidos y mantener consistencia en la información.

Se decidió que el formulario de creación de tickets solo permita ingresar título, descripción y categoría. Los campos de usuario, fecha de creación y estado inicial son asignados automáticamente por el sistema.

## 7. Modelo de clases UML

```mermaid
classDiagram
    class User {
        int id
        string username
        string email
        string password
    }

    class Categoria {
        int id
        string nombre
        string descripcion
    }

    class Ticket {
        int id
        string titulo
        string descripcion
        string estado
        datetime fecha_creacion
        string respuesta_admin
    }

    User "1" --> "*" Ticket : crea
    Categoria "1" --> "*" Ticket : clasifica
```

## 8. Modelo relacional de base de datos

```mermaid
erDiagram
    AUTH_USER ||--o{ TICKETS_TICKET : crea
    TICKETS_CATEGORIA ||--o{ TICKETS_TICKET : clasifica

    AUTH_USER {
        int id PK
        string username
        string password
        string email
    }

    TICKETS_CATEGORIA {
        int id PK
        string nombre
        string descripcion
    }

    TICKETS_TICKET {
        int id PK
        int usuario_id FK
        int categoria_id FK
        string titulo
        text descripcion
        string estado
        datetime fecha_creacion
        text respuesta_admin
    }
```

## 9. Flujo principal del sistema

```mermaid
flowchart TD
    A[Usuario ingresa al sistema] --> B[Inicia sesión]
    B --> C{¿Autenticación válida?}
    C -- No --> D[Permanece en login]
    C -- Sí --> E[Accede al sistema]
    E --> F[Crea un ticket]
    F --> G[Sistema asigna usuario, fecha y estado Abierto]
    G --> H[Usuario consulta Mis tickets]
    H --> I[Usuario abre detalle de un ticket propio]
    I --> J[Administrador revisa ticket en Django Admin]
    J --> K[Administrador cambia estado y registra respuesta]
    K --> L[Usuario visualiza estado y respuesta en el detalle]
```

## 10. Categorías propuestas

Las categorías propuestas para clasificar los tickets son:

| Categoría | Descripción |
|---|---|
| Soporte técnico | Solicitudes relacionadas con fallas técnicas, errores de funcionamiento o problemas operativos del sistema. |
| Accesos y usuarios | Solicitudes relacionadas con inicio de sesión, usuarios, permisos o acceso al sistema. |
| Errores del sistema | Reportes de comportamientos inesperados, errores visibles o fallas de la aplicación. |
| Solicitudes administrativas | Requerimientos relacionados con procesos internos, información administrativa o soporte institucional. |
| Consultas generales | Preguntas o solicitudes que no pertenecen claramente a una categoría específica. |

Estas categorías fueron definidas con base en un entorno institucional simple, buscando cubrir los casos de soporte más comunes sin agregar complejidad innecesaria al sistema.

## 11. Seguridad y control de acceso

El sistema restringe la creación y consulta de tickets únicamente a usuarios autenticados.

Para evitar accesos no autorizados, las vistas de listado y detalle filtran los tickets por el usuario autenticado. De esta manera, un usuario no puede consultar tickets creados por otros usuarios.

El estado del ticket no se incluye en el formulario de creación. Este campo se asigna automáticamente como “Abierto” y solo puede ser modificado por el administrador desde Django Admin.

## 12. Supuestos

- Los usuarios serán creados previamente por el administrador.
- Las categorías iniciales podrán ser creadas desde Django Admin.
- El sistema será ejecutado localmente usando SQLite.
- No se implementa registro público de usuarios.
- No se implementa recuperación de contraseña.
- No se implementan notificaciones por correo electrónico.
- La interfaz será simple y basada en plantillas HTML de Django.
- El sistema se desarrolla como una prueba técnica de alcance limitado.

## 13. Uso de herramientas de inteligencia artificial

Se utilizó ChatGPT como herramienta de apoyo para orientar el diseño inicial del proyecto, revisar buenas prácticas en Django, validar aspectos básicos de seguridad y apoyar la redacción de documentación técnica.

La implementación, las pruebas, las decisiones finales de diseño y la comprensión del código fueron responsabilidad del aplicante.
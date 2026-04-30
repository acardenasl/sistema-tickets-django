# Sistema Básico de Tickets de Soporte

Proyecto de prueba técnica para implementar un sistema básico de tickets usando Django.

Este proyecto corresponde a una prueba técnica para desarrollar una aplicación web sencilla en Django que permita a usuarios autenticados crear tickets de soporte, consultar sus propios tickets y revisar las respuestas del administrador.

El sistema utiliza la autenticación nativa de Django, Django Admin para la gestión administrativa y SQLite como base de datos local.

---

## 1. Objetivo del proyecto

El objetivo es implementar un sistema básico de tickets de soporte con dos tipos principales de uso:

- Usuario cliente:
  - Iniciar sesión.
  - Crear tickets de soporte.
  - Consultar únicamente los tickets que ha creado.
  - Ver el estado y la respuesta del administrador.

- Usuario administrador:
  - Ingresar al panel de administración de Django.
  - Consultar los tickets creados por los usuarios.
  - Cambiar el estado de los tickets.
  - Registrar una respuesta administrativa.

---

## 2. Funcionalidades implementadas

### Autenticación

El sistema utiliza el sistema de autenticación incluido en Django.

Funcionalidades incluidas:

- Login de usuarios.
- Logout de usuarios.
- Restricción de acceso a vistas privadas.
- Uso de sesiones de Django.
- Protección CSRF en formularios.

### Gestión de tickets por usuario

El usuario autenticado puede:

- Crear un nuevo ticket.
- Seleccionar una categoría.
- Ingresar título y descripción.
- Consultar la lista de sus tickets.
- Ver el detalle de cada ticket.
- Consultar el estado asignado por el administrador.
- Ver la respuesta del administrador, si existe.

El usuario no puede seleccionar ni modificar el estado del ticket.

### Gestión administrativa

Desde Django Admin, el administrador puede:

- Crear y gestionar categorías.
- Consultar tickets creados por los usuarios.
- Filtrar tickets por estado, categoría y fecha.
- Buscar tickets por título, descripción o usuario.
- Cambiar el estado del ticket.
- Registrar una respuesta administrativa.

---

## 3. Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML básico
- Django Forms
- Django Admin
- Django Authentication System

---

## 4. Estructura general del proyecto

```text
sistema-tickets-django/
├── manage.py
├── requirements.txt
├── README.md
├── documento_diseno.md
├── soporte_tickets/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── tickets/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    └── templates/
        └── tickets/
            ├── base.html
            ├── login.html
            ├── crear_ticket.html
            ├── mis_tickets.html
            └── detalle_ticket.html
```

Nota: `db.sqlite3` es la base de datos local generada después de ejecutar las migraciones. Puede existir en el ambiente local de desarrollo, pero no es indispensable incluirla en el repositorio si el evaluador va a ejecutar las migraciones desde cero.

---

## 5. Modelos implementados

### Categoria

Representa el tipo de solicitud asociada a un ticket.

Campos principales:

- `nombre`: nombre de la categoría.
- `descripcion`: descripción opcional de la categoría.

### Ticket

Representa una solicitud de soporte creada por un usuario.

Campos principales:

- `usuario`: usuario autenticado que creó el ticket.
- `categoria`: categoría asociada al ticket.
- `titulo`: título breve de la solicitud.
- `descripcion`: descripción detallada del problema o solicitud.
- `estado`: estado actual del ticket.
- `fecha_creacion`: fecha automática de creación.
- `respuesta_admin`: respuesta registrada por el administrador.

Estados disponibles:

- Abierto
- En espera
- Aprobado
- Rechazado

El estado inicial de todo ticket es `Abierto`.

---

## 6. Categorías propuestas

Las categorías definidas para el sistema son:

1. Soporte técnico  
2. Accesos y usuarios  
3. Errores del sistema  
4. Solicitudes administrativas  
5. Consultas generales  

Estas categorías permiten clasificar tickets de manera simple y suficientemente clara para un sistema básico de soporte.

---

## 7. Instalación y ejecución del proyecto

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/acardenasl/sistema-tickets-django.git
cd sistema-tickets-django
```

También se puede descargar el proyecto en ZIP y abrirlo localmente.

### 2. Crear entorno virtual

En Windows PowerShell:

```bash
python -m venv venv
```

Activar el entorno virtual:

```bash
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear usuario administrador

```bash
python manage.py createsuperuser
```

Seguir las instrucciones de la terminal para definir usuario, correo y contraseña.

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/login/
```

---

## 8. Rutas principales

```text
/admin/
```

Panel administrativo de Django.

```text
/login/
```

Inicio de sesión de usuarios.

```text
/logout/
```

Cierre de sesión de usuarios.

```text
/ticket/crear/
```

Formulario para crear un nuevo ticket.

```text
/mis-tickets/
```

Listado de tickets creados por el usuario autenticado.

```text
/mis-tickets/<id_ticket>/
```

Detalle de un ticket específico.

---

## 9. Credenciales de prueba

Para las pruebas locales se utilizaron usuarios de ejemplo.

### Usuario administrador

```text
Usuario: admin
Contraseña: Admin123
```

### Usuarios cliente

```text
Usuario: Juan.Perez
Contraseña: jp123456
```

```text
Usuario: Pepito.Perez
Contraseña: pp123456
```

Nota: estas credenciales corresponden al ambiente local de prueba. Si la base de datos no se incluye en la entrega, los usuarios deben ser creados nuevamente desde Django Admin o mediante `createsuperuser`.

---

## 10. Creación de usuario cliente

Después de crear el superusuario, ingresar a:

```text
http://127.0.0.1:8000/admin/
```

Luego ir a:

```text
Authentication and Authorization > Users > Add user
```

Crear un usuario cliente normal, sin permisos de staff ni superusuario.

Este usuario podrá iniciar sesión en `/login/`, crear tickets y consultar únicamente sus propios tickets.

---

## 11. Creación de categorías

Las categorías se pueden crear desde Django Admin ingresando a:

```text
Tickets > Categorías > Add Categoría
```

Categorías recomendadas:

- Soporte técnico
- Accesos y usuarios
- Errores del sistema
- Solicitudes administrativas
- Consultas generales

---

## 12. Flujo de uso

### Usuario cliente

1. Ingresar a `/login/`.
2. Iniciar sesión con un usuario cliente.
3. Ir a `/ticket/crear/`.
4. Crear un ticket con título, descripción y categoría.
5. Consultar el ticket en `/mis-tickets/`.
6. Abrir el detalle del ticket para ver estado y respuesta administrativa.

### Usuario administrador

1. Ingresar a `/admin/`.
2. Iniciar sesión con el superusuario.
3. Ir a la sección `Tickets`.
4. Abrir un ticket.
5. Cambiar su estado.
6. Escribir una respuesta administrativa.
7. Guardar los cambios.

---

## 13. Seguridad implementada

El sistema implementa controles básicos de seguridad usando herramientas nativas de Django:

- Las vistas privadas requieren autenticación mediante `@login_required`.
- Los usuarios solo pueden consultar sus propios tickets.
- La vista de listado filtra por el usuario autenticado.
- La vista de detalle valida que el ticket pertenezca al usuario actual.
- Los formularios usan protección CSRF.
- El estado del ticket no está disponible en el formulario del usuario.
- La respuesta administrativa solo se gestiona desde Django Admin.

La validación de acceso a tickets ajenos se implementó mediante consultas filtradas por usuario:

```python
Ticket.objects.filter(usuario=request.user)
```

y:

```python
get_object_or_404(Ticket, id=id_ticket, usuario=request.user)
```

Esto evita que un usuario autenticado pueda acceder a tickets de otro usuario modificando manualmente el ID en la URL.

---

## 14. Supuestos del proyecto

- Los usuarios son creados previamente por el administrador.
- No se permite registro público de usuarios.
- El sistema es una aplicación básica de soporte, sin manejo de prioridades.
- No se implementan notificaciones por correo.
- No se implementa recuperación de contraseña.
- No se implementa historial detallado de cambios.
- No se implementa API REST.
- Las categorías son administradas desde Django Admin.
- SQLite es suficiente para el alcance de la prueba técnica.

---

## 15. Pruebas realizadas

Se realizaron las siguientes pruebas manuales:

- Inicio de sesión con usuario administrador.
- Inicio de sesión con usuario cliente.
- Creación de categorías desde Django Admin.
- Creación de tickets desde usuario cliente.
- Validación de estado inicial `Abierto`.
- Consulta de listado de tickets por usuario.
- Consulta de detalle de ticket.
- Cambio de estado desde Django Admin.
- Registro de respuesta administrativa.
- Visualización de la respuesta por parte del usuario cliente.
- Validación de que un usuario no pueda acceder a tickets de otro usuario.
- Cierre de sesión usando formulario POST.

---

## 16. Uso de inteligencia artificial

Durante el desarrollo se utilizó inteligencia artificial como herramienta de apoyo para:

- Revisar buenas prácticas en Django.
- Apoyar la orientación técnica en procesos de Django
- Apoyar la redacción del README y del documento de diseño.
- Validar decisiones de seguridad, rutas, modelos y formularios.

La implementación fue revisada, ejecutada y probada localmente durante el desarrollo.
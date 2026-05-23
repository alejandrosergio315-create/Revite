# Proyecto ReViTe

## Descripción del proyecto

ReViTe es una aplicación desarrollada en **Python** utilizando **Flet** para la interfaz gráfica y **SQLite** para la persistencia de datos.

El sistema permite gestionar reservas de transporte mediante operaciones CRUD (**Crear, Leer, Actualizar y Eliminar**), facilitando el registro de usuarios y la administración de sus reservas.

---

# Objetivo del proyecto

Desarrollar una aplicación funcional que permita a los usuarios:

- Registrarse en el sistema.
- Buscar su información mediante su número de cédula.
- Crear nuevas reservas de transporte.
- Consultar sus reservas realizadas.
- Confirmar reservas.
- Eliminar reservas.
- Visualizar su perfil.

---

# Tecnologías utilizadas

Para el desarrollo del proyecto se utilizaron las siguientes tecnologías:

- **Python 3**
- **Flet** (interfaz gráfica)
- **SQLite** (base de datos local)
- **Programación Orientada a Objetos (POO)**

---

# Funcionalidades principales

## Registro de usuarios

Permite registrar nuevos usuarios ingresando la siguiente información:

- Cédula
- Nombre
- Apellido
- Celular

Los datos quedan almacenados en la base de datos.

---

## Búsqueda de clientes

El sistema permite consultar usuarios ya registrados mediante su número de cédula.

---

## Creación de reservas

El usuario puede crear una reserva seleccionando:

- Destino (**Bogotá, Ibagué o Espinal**)
- Hora de salida
- Fecha
- Vehículo disponible

---

## Mis reservas

Permite visualizar el historial de reservas del usuario actual.

Desde esta sección se pueden realizar las siguientes acciones:

- **Confirmar reserva**
- **Eliminar reserva**

---

## Mi perfil

Muestra la información del usuario registrado:

- Nombre
- Cédula
- Celular

---

# Implementación CRUD

## CREATE (Crear)

Se implementó para:

- Registrar usuarios nuevos.
- Crear nuevas reservas.

---

## READ (Leer)

Se implementó para:

- Buscar usuarios por cédula.
- Visualizar las reservas del usuario.
- Mostrar el perfil del usuario.

---

## UPDATE (Actualizar)

Se implementó mediante:

- Confirmación de reservas.

---

## DELETE (Eliminar)

Se implementó mediante:

- Eliminación de reservas existentes.

---

# Persistencia de datos

Para el almacenamiento de información se utilizó **SQLite**, una base de datos ligera y fácil de integrar con Python.

### Tablas principales:

- **usuarios**
- **reservas**

Los datos permanecen almacenados aunque la aplicación sea cerrada.

---

# Interfaz gráfica

La interfaz fue desarrollada con **Flet**, permitiendo una experiencia visual interactiva y organizada.

La aplicación cuenta con tres secciones principales:

- **Reservar**
- **Mis reservas**
- **Mi perfil**

---

# Validaciones implementadas

Se implementaron validaciones para garantizar la correcta entrada de datos:

- Verificación de campos obligatorios.
- Validación de selección de destino.
- Validación de fecha.
- Validación de selección de vehículo.
- Prevención de registros incompletos.

Además, el sistema muestra mensajes de error o confirmación según la acción realizada.

---

# Instalación y ejecución

## Requisitos

Tener instalado:

- **Python 3**

---

## Instalación de dependencias

Ejecutar el siguiente comando:

```bash
pip install flet
```

---

## Ejecución del proyecto

Desde la carpeta principal ejecutar:

```bash
python main.py
```

---

# Estructura del proyecto

```text
Proyecto_ReViTe/
│
├── main.py
│
├── models/
│   ├── clientes.py
│   ├── carros.py
│   └── reservas.py
│
├── views/
│   └── booking_view.py
│
├── controllers/
│   ├── mensajes.py
│   └── validaciones.py
│
└── database/
    └── main_sqlite3.py
```

---

# Pruebas realizadas

Se verificó el correcto funcionamiento de las siguientes funcionalidades:

- Registro de usuarios.
- Búsqueda de clientes.
- Creación de reservas.
- Confirmación de reservas.
- Eliminación de reservas.
- Visualización del historial de reservas.
- Persistencia correcta de los datos en SQLite.

---

# Seguridad

Se implementaron validaciones de entrada para evitar errores y mantener la integridad de la información almacenada.

Entre ellas:

- Prevención de campos vacíos.
- Validación básica de datos ingresados.
- Control de acciones del usuario dentro del sistema.

---

# Autor

**Sergio Villalobos**

---

# Estado del proyecto

Proyecto funcional y en desarrollo continuo.
# Vibra: Tienda de Discos Online

## 🎶 Sobre el Proyecto

Vibra es una tienda en línea dedicada a conectar a los amantes de la música con una vasta colección de discos. Desde los últimos lanzamientos hasta los clásicos atemporales, Vibra ofrece una plataforma intuitiva para explorar, descubrir y adquirir música de diversos géneros y artistas. Creada con el framework Flask de Python, esta aplicación permite a los usuarios gestionar su colección de discos, añadir nuevos títulos a su carrito de compras, y realizar pedidos con facilidad.

## 🛠️ Enfoque y Metodología

La aplicación se ha desarrollado utilizando Python y Flask, optando por una arquitectura MVC para separar la lógica de la aplicación, la interfaz de usuario, y la interacción con la base de datos. Esta estructura facilita el mantenimiento y la escalabilidad del proyecto.

## 🏗️ Arquitectura del Sistema

- **Modelo**: Utiliza SQLAlchemy para modelar y gestionar la base de datos SQLite, centrada en el modelo `Discos`.
- **Vista**: Implementa plantillas HTML renderizadas en el servidor para presentar dinámicamente los datos.
- **Controlador**: Flask gestiona las rutas y las solicitudes del cliente, vinculando las vistas con los modelos de datos.

## 💻 Tecnologías Utilizadas

El proyecto Vibra integra una variedad de tecnologías en el Front y el Back para proporcionar una experiencia de usuario rica y una arquitectura de aplicación robusta.

### Backend

- **Python**: Lenguaje de programación principal para la lógica del servidor.
- **Flask**: Microframework de Python utilizado para manejar solicitudes HTTP, renderizar plantillas y gestionar la sesión del usuario.
- **SQLite**: Sistema de gestión de bases de datos ligero, utilizado para almacenar datos de discos y usuarios.
- **SQLAlchemy**: ORM (Object Relational Mapping) de Python que facilita la interacción entre objetos Python y la base de datos, mejorando la eficiencia del desarrollo y mantenimiento del código.
- **Flask-SQLAlchemy**: Extensión de Flask que añade soporte para SQLAlchemy, simplificando la configuración y uso de la base de datos.

### Frontend

- **HTML5**: Lenguaje de marcado utilizado para estructurar el contenido de las páginas web.
- **CSS3**: Lenguaje de hojas de estilo utilizado para definir la presentación visual y el diseño de las páginas web. 
- **Tailwind CSS**: Marco de trabajo CSS que se ha utilizado para diseñar y personalizar la interfaz de usuario de Vibra, proporcionando un enfoque altamente modular y personalizable para los estilos. Gracias a Tailwind CSS, el diseño de la aplicación es tanto responsivo como estéticamente agradable, permitiendo un desarrollo ágil del frontend con una gran coherencia visual y facilidad de mantenimiento.


Esta combinación de tecnologías asegura que Vibra sea una aplicación web moderna, eficiente y fácil de mantener, permitiendo a los usuarios explorar, gestionar y comprar discos de música de manera intuitiva y placentera.


## 🚀 Instrucciones para Ejecutar

### Pre-requisitos

- Python 3.x
- Flask
- Flask-SQLAlchemy

### Instalación

1. Clone el repositorio o descargue el código fuente.
2. Instale las dependencias necesarias con `pip install flask flask-sqlalchemy`.
3. Inicialice la base de datos con `python init_db.py`.

### Ejecución

Ejecute `py app.py` desde su terminal y acceda a la aplicación a través de `http://localhost:5000`.

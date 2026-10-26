# Alcance del producto

## 1. Objetivo del alcance

Este documento define qué se incluirá en la primera versión del blog de
robótica, qué queda expresamente fuera y cuáles son los límites funcionales y
técnicos de la entrega. Su finalidad es mantener el desarrollo centrado en una
experiencia sencilla de publicación y lectura, evitando añadir funciones que
no sean necesarias para cumplir el PRD.

El producto permitirá que las personas visitantes consulten artículos de
robótica y conozcan al autor, mientras que el editor podrá mantener el
contenido mediante el panel administrativo estándar de Django.

## 2. Objetivos de la primera versión

La primera versión debe:

- ofrecer una portada clara con los artículos publicados más recientes;
- permitir abrir y leer cada artículo en una página propia;
- proporcionar una sección «Sobre mí» editable;
- ofrecer una navegación sencilla, visible y comprensible;
- funcionar correctamente en móviles y ordenadores;
- priorizar la legibilidad, la accesibilidad y el contenido;
- permitir al editor gestionar el contenido sin modificar plantillas;
- ocultar los artículos no publicados a las personas visitantes;
- mostrar una respuesta 404 adecuada para artículos inexistentes.

## 3. Personas usuarias y permisos

### 3.1. Visitante

El visitante podrá:

- acceder a la portada;
- consultar el listado de artículos publicados;
- abrir un artículo mediante su enlace;
- leer el título, la fecha, la autoría y el contenido del artículo;
- consultar la sección «Sobre mí»;
- navegar entre la portada, los artículos y «Sobre mí».

El visitante no podrá crear cuentas, editar contenido, publicar artículos ni
acceder a las operaciones de administración.

### 3.2. Editor del sitio

El editor será una persona autorizada para utilizar Django Admin. Podrá:

- crear artículos;
- modificar artículos existentes;
- retirar o despublicar artículos;
- definir el estado de publicación;
- actualizar la presentación del autor;
- sustituir o eliminar el contenido inicial de ejemplo.

La primera versión contempla un único contexto editorial y no incluye
múltiples roles ni flujos de aprobación.

## 4. Funcionalidades incluidas

### 4.1. Portada

La ruta `/` mostrará:

- el nombre del blog;
- una lista de artículos publicados;
- los artículos ordenados del más nuevo al más antiguo;
- el título de cada artículo;
- la fecha de publicación;
- un extracto;
- un enlace descriptivo al artículo completo.

Cuando no haya artículos publicados, la portada mostrará un mensaje
informativo que explique la ausencia de contenido. No se presentará una lista
vacía sin contexto.

### 4.2. Detalle del artículo

La ruta `/articulos/<slug>/` mostrará una página individual con:

- título;
- fecha de publicación;
- autoría;
- contenido completo;
- párrafos y subtítulos conservados de forma legible;
- navegación para volver a la portada.

El identificador de la URL será un slug legible. Una ruta inexistente o
correspondiente a un artículo no publicado no expondrá contenido público y
deberá devolver una respuesta HTTP 404 adecuada.

### 4.3. Sección «Sobre mí»

La ruta `/sobre-mi/` mostrará una presentación breve del autor. El contenido:

- será accesible desde la navegación principal;
- tendrá una estructura legible;
- podrá actualizarse desde Django Admin;
- podrá sustituirse por el texto definitivo del autor sin editar plantillas.

La primera versión contempla una única presentación principal del sitio.

### 4.4. Navegación

Las páginas públicas ofrecerán, como mínimo:

- un enlace a la portada;
- un enlace a «Sobre mí»;
- enlaces desde la portada a cada artículo;
- un enlace desde el artículo para volver a la portada.

Los enlaces tendrán nombres claros y funcionarán sin JavaScript. La
navegación se mantendrá disponible en las páginas principales del sitio.

### 4.5. Gestión editorial

El contenido se gestionará mediante el panel administrativo estándar de
Django. El editor podrá administrar artículos y la presentación del autor con
las operaciones básicas de alta, edición y retirada.

El panel `/admin/` estará restringido a usuarios autorizados. No habrá
registro público ni operaciones de edición disponibles para visitantes
anónimos.

## 5. Modelo de contenido incluido

### 5.1. Artículo

Cada artículo incluirá, como mínimo:

- título;
- slug o identificador legible para la URL;
- contenido;
- autoría;
- fecha de publicación;
- estado de publicación.

Los artículos publicados podrán aparecer en las páginas públicas. Los
borradores o artículos retirados solo estarán disponibles para el editor
autenticado mediante el panel administrativo, según la configuración de
permisos de Django.

El contenido deberá admitir una estructura básica de lectura con párrafos y
subtítulos.

### 5.2. Presentación del autor

El sitio incluirá un contenido editable para la sección «Sobre mí». En la
primera versión habrá una única presentación principal, suficiente para
describir brevemente al autor y su relación con la robótica.

### 5.3. Contenido inicial

La entrega incluirá artículos de ejemplo relacionados con robótica y una
presentación inicial del autor. Este contenido tendrá carácter demostrativo y
podrá sustituirse o eliminarse desde Django Admin.

## 6. Rutas y superficies del producto

| Ruta | Superficie | Alcance |
|---|---|---|
| `/` | Portada | Nombre del blog y artículos publicados |
| `/sobre-mi/` | Sobre mí | Presentación editable del autor |
| `/articulos/<slug>/` | Detalle de artículo | Lectura de un artículo publicado |
| `/admin/` | Administración | Gestión restringida de contenido |

Además, deberán contemplarse respuestas adecuadas para rutas de artículos
inexistentes, incluyendo el estado HTTP 404.

## 7. Requisitos de experiencia y calidad

### 7.1. Adaptabilidad

Las páginas deberán poder utilizarse en pantallas pequeñas y grandes sin
perder contenido, controles ni navegación. Se evitará el desplazamiento
horizontal innecesario.

### 7.2. Legibilidad

La interfaz priorizará la lectura prolongada mediante:

- tipografía legible;
- contraste suficiente;
- espaciado coherente;
- longitud de línea razonable;
- jerarquía visual clara;
- separación reconocible entre párrafos y subtítulos.

### 7.3. Accesibilidad

La implementación utilizará HTML semántico, una jerarquía de encabezados
coherente, enlaces descriptivos y controles utilizables con teclado. La
navegación básica no dependerá de JavaScript.

### 7.4. Rendimiento y arquitectura

Las páginas informativas se renderizarán en el servidor con Django. No se
añadirán dependencias de JavaScript salvo que una necesidad concreta del
producto lo justifique.

### 7.5. Seguridad editorial

Las operaciones de administración deberán permanecer restringidas a usuarios
autorizados. Los visitantes anónimos no tendrán acceso a la edición y los
artículos no publicados no deberán aparecer en las páginas públicas.

## 8. Solución técnica dentro del alcance

La primera versión contempla:

- Django para el backend y el renderizado de plantillas;
- modelos Django para artículos y presentación del autor;
- migraciones para persistir dichos modelos;
- Django Admin como interfaz de gestión editorial;
- plantillas HTML semánticas;
- CSS adaptable;
- SQLite para el desarrollo inicial.

La elección de la base de datos de producción y los detalles del despliegue
quedan fuera de este documento y dependerán del entorno de publicación.

## 9. Fuera de alcance

No forman parte de la primera versión:

- cuentas, perfiles o registro de lectores;
- comentarios o respuestas en los artículos;
- suscripciones, boletines o notificaciones;
- buscador de artículos;
- etiquetas, categorías o filtros avanzados, salvo que sean necesarios para
  cumplir el alcance definido;
- funciones de interacción social;
- compartir automáticamente en redes sociales;
- reacciones, favoritos o valoraciones;
- flujos editoriales avanzados de revisión;
- programación de publicaciones;
- múltiples roles editoriales;
- analítica avanzada o paneles de métricas;
- API pública;
- aplicación móvil nativa;
- internacionalización o traducciones;
- personalización avanzada del tema visual;
- selección definitiva de infraestructura o base de datos de producción.

## 10. Dependencias y supuestos

El alcance se basa en los siguientes supuestos:

- el idioma inicial del sitio será el español;
- el tema principal será la robótica;
- habrá una presentación principal del autor;
- el editor utilizará Django Admin para mantener el contenido;
- el contenido inicial será de ejemplo y podrá reemplazarse;
- no se requiere autenticación para leer contenido público;
- la base de datos inicial será SQLite;
- la identidad visual, el dominio y el entorno de despliegue se decidirán
  posteriormente.

## 11. Criterios de finalización

El alcance se considerará cubierto cuando:

- la ruta `/` muestre el nombre del blog y los artículos publicados en orden
  descendente por fecha;
- cada artículo listado incluya título, fecha, extracto y enlace;
- un visitante pueda leer un artículo completo desde su URL;
- el artículo muestre título, fecha, autoría y contenido;
- los párrafos y subtítulos se presenten de forma legible;
- `/sobre-mi/` sea accesible desde la navegación principal;
- desde un artículo se pueda volver a la portada;
- una portada sin artículos muestre un mensaje informativo;
- una ruta de artículo inexistente responda con HTTP 404;
- los artículos no publicados no aparezcan públicamente;
- el editor pueda crear, editar y retirar artículos desde Django Admin;
- el editor pueda actualizar la presentación del autor desde Django Admin;
- las páginas funcionen en móvil y escritorio sin desplazamiento horizontal
  innecesario;
- no exista registro público ni edición para visitantes anónimos.

## 12. Resultado esperado

La entrega será un blog de robótica pequeño, mantenible y centrado en la
lectura. Una persona podrá descubrir un artículo desde la portada, leerlo
completo, consultar quién lo escribe y desplazarse por el sitio sin
obstáculos. El editor podrá mantener el contenido mediante Django Admin sin
necesidad de cambiar manualmente las plantillas.

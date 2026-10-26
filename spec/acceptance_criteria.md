# Criterios de aceptación

## 1. Propósito

Este documento define las condiciones verificables que debe cumplir la
primera versión del blog de robótica para considerarse aceptada. Los criterios
se derivan del PRD, del alcance del producto y de la visión del sitio.

Salvo que se indique lo contrario, «visitante» significa una persona sin
autenticación y «editor» significa una persona autorizada para acceder a
Django Admin.

## 2. Requisitos previos de validación

Para ejecutar las comprobaciones:

- la aplicación Django debe estar instalada y configurada;
- deben existir las rutas públicas definidas en el alcance;
- debe existir al menos un usuario autorizado para Django Admin;
- deben poder crearse artículos publicados y no publicados;
- debe existir contenido inicial de ejemplo o poder cargarse mediante el
  panel administrativo;
- las pruebas deben poder realizarse sin JavaScript para la navegación básica.

## 3. Criterios de aceptación funcionales

### CA-01. Acceso a la portada

**Dado** que la aplicación está disponible  
**Cuando** un visitante accede a `/`  
**Entonces** recibe la portada del blog con una respuesta correcta  
**Y** se muestra el nombre del blog  
**Y** la navegación principal está disponible.

### CA-02. Listado de artículos publicados

**Dado** que existen varios artículos publicados  
**Cuando** un visitante accede a `/`  
**Entonces** se muestran los artículos publicados  
**Y** aparecen ordenados por fecha de publicación de más reciente a más
antiguo  
**Y** cada elemento muestra, como mínimo, título, fecha y extracto  
**Y** cada elemento incluye un enlace al artículo completo.

### CA-03. Exclusión de artículos no publicados de la portada

**Dado** que existen artículos publicados y no publicados  
**Cuando** un visitante accede a `/`  
**Entonces** solo aparecen los artículos publicados  
**Y** ningún borrador o artículo retirado aparece en el listado público.

### CA-04. Portada sin artículos

**Dado** que no existen artículos publicados  
**Cuando** un visitante accede a `/`  
**Entonces** la portada se renderiza correctamente  
**Y** muestra un mensaje informativo sobre la ausencia de artículos  
**Y** no muestra una lista vacía sin explicación.

### CA-05. Acceso al detalle de un artículo

**Dado** que existe un artículo publicado con un slug válido  
**Cuando** un visitante accede a `/articulos/<slug>/`  
**Entonces** se muestra la página individual del artículo  
**Y** se muestran el título, la fecha de publicación, la autoría y el
contenido completo  
**Y** la página identifica claramente que se trata de un artículo.

### CA-06. Estructura del contenido del artículo

**Dado** que el contenido de un artículo contiene varios párrafos y
subtítulos  
**Cuando** se muestra su página individual  
**Entonces** los párrafos se conservan como bloques diferenciados  
**Y** los subtítulos mantienen una jerarquía reconocible  
**Y** el contenido se puede leer sin depender de estilos o JavaScript.

### CA-07. Artículo inexistente

**Dado** que no existe un artículo para el slug solicitado  
**Cuando** un visitante accede a `/articulos/<slug>/`  
**Entonces** la aplicación responde con HTTP 404  
**Y** muestra una página de no encontrado adecuada  
**Y** no muestra datos de otro artículo ni un contenido de éxito.

### CA-08. Artículo no publicado solicitado directamente

**Dado** que existe un artículo no publicado  
**Cuando** un visitante no autenticado accede a su URL  
**Entonces** la aplicación responde como recurso no disponible públicamente,
preferentemente con HTTP 404  
**Y** no revela su título, contenido, autoría ni fecha.

### CA-09. Acceso a «Sobre mí»

**Dado** que un visitante navega por el sitio  
**Cuando** accede a `/sobre-mi/`  
**Entonces** se muestra una página identificable como «Sobre mí»  
**Y** se muestra la presentación del autor  
**Y** la presentación es legible y está estructurada como contenido principal.

### CA-10. Enlace principal a «Sobre mí»

**Dado** que un visitante se encuentra en la portada o en un artículo  
**Cuando** consulta la navegación principal  
**Entonces** encuentra un enlace con el nombre «Sobre mí»  
**Y** el enlace lleva a `/sobre-mi/`.

### CA-11. Navegación hacia la portada

**Dado** que un visitante está en un artículo o en «Sobre mí»  
**Cuando** utiliza el enlace de portada o de regreso  
**Entonces** vuelve a `/`  
**Y** no necesita utilizar JavaScript para completar la navegación.

### CA-12. Enlaces descriptivos

**Dado** que se muestran enlaces de navegación o de artículos  
**Cuando** un visitante los consulta  
**Entonces** sus textos describen claramente el destino  
**Y** no dependen únicamente de iconos, colores o contexto visual para ser
comprendidos.

## 4. Criterios de aceptación del contenido y la gestión editorial

### CA-13. Campos mínimos del artículo

**Dado** que el editor crea o modifica un artículo  
**Entonces** el sistema permite gestionar, como mínimo:

- título;
- slug legible para la URL;
- contenido;
- autoría;
- fecha de publicación;
- estado de publicación.

**Y** un artículo válido puede guardarse y utilizarse en las páginas públicas
cuando está publicado.

### CA-14. Creación de artículos desde Django Admin

**Dado** que el editor está autenticado y autorizado  
**Cuando** crea un artículo desde `/admin/` y lo marca como publicado  
**Entonces** el artículo puede guardarse  
**Y** aparece en la portada según su fecha  
**Y** se puede abrir mediante su slug.

### CA-15. Edición de artículos

**Dado** que existe un artículo gestionado desde Django Admin  
**Cuando** el editor modifica su título, contenido, autoría, fecha o estado  
**Entonces** los cambios se guardan correctamente  
**Y** las páginas públicas reflejan los cambios cuando el artículo está
publicado.

### CA-16. Retirada o despublicación

**Dado** que un artículo publicado aparece en la portada  
**Cuando** el editor lo retira o lo marca como no publicado  
**Entonces** deja de aparecer en la portada  
**Y** deja de estar disponible para visitantes no autenticados.

### CA-17. Gestión de «Sobre mí»

**Dado** que el editor está autenticado y autorizado  
**Cuando** actualiza la presentación del autor desde Django Admin  
**Entonces** puede guardar el nuevo texto  
**Y** el contenido actualizado aparece en `/sobre-mi/`  
**Y** no es necesario modificar una plantilla.

### CA-18. Contenido inicial sustituible

**Dado** que la aplicación se entrega con contenido de ejemplo  
**Cuando** el editor lo sustituye o lo elimina desde Django Admin  
**Entonces** el contenido público refleja la gestión realizada  
**Y** el sitio no depende de los textos iniciales para funcionar.

## 5. Criterios de aceptación de acceso y seguridad

### CA-19. Acceso restringido al panel

**Dado** que un visitante no está autenticado o no tiene permisos  
**Cuando** intenta acceder a `/admin/`  
**Entonces** no puede realizar operaciones de gestión editorial  
**Y** Django aplica su mecanismo estándar de autenticación y autorización.

### CA-20. Ausencia de registro público

**Dado** que un visitante utiliza el sitio público  
**Cuando** navega por las páginas disponibles  
**Entonces** no encuentra un flujo de registro de lectores  
**Y** no puede crear una cuenta pública para publicar o editar contenido.

### CA-21. Separación entre contenido público y editorial

**Dado** que existen artículos en distintos estados  
**Cuando** un visitante utiliza las rutas públicas  
**Entonces** solo puede consultar artículos publicados  
**Y** los borradores no se filtran mediante la portada, enlaces o acceso
directo.

## 6. Criterios de aceptación de experiencia y accesibilidad

### CA-22. Diseño adaptable

**Dado** que el sitio se visualiza en una pantalla pequeña o grande  
**Cuando** un visitante consulta la portada, un artículo o «Sobre mí»  
**Entonces** el contenido permanece visible y utilizable  
**Y** la navegación no se pierde  
**Y** no aparece desplazamiento horizontal innecesario.

### CA-23. Legibilidad

**Dado** que un visitante lee la portada o un artículo  
**Entonces** la tipografía es legible  
**Y** existe contraste suficiente entre texto y fondo  
**Y** el espaciado permite distinguir los bloques de contenido  
**Y** la longitud de línea favorece la lectura prolongada.

### CA-24. HTML semántico y encabezados

**Dado** que se inspecciona la estructura de una página pública  
**Entonces** se utilizan elementos HTML semánticos apropiados  
**Y** existe una jerarquía de encabezados coherente  
**Y** el contenido principal se distingue de la navegación.

### CA-25. Uso con teclado

**Dado** que un visitante utiliza únicamente el teclado  
**Cuando** recorre los enlaces y controles disponibles  
**Entonces** puede alcanzar los elementos interactivos  
**Y** el orden de navegación es comprensible  
**Y** los elementos enfocados se pueden identificar.

### CA-26. Independencia de JavaScript

**Dado** que JavaScript está deshabilitado  
**Cuando** un visitante utiliza la navegación básica  
**Entonces** puede acceder a la portada, a «Sobre mí» y a los artículos
mediante enlaces HTML normales  
**Y** el contenido principal sigue siendo accesible.

## 7. Criterios de aceptación técnicos y de robustez

### CA-27. Renderizado del servidor

**Dado** que un visitante solicita una página informativa  
**Cuando** Django procesa la solicitud  
**Entonces** la página se renderiza en el servidor mediante vistas y plantillas
de Django  
**Y** no requiere una aplicación JavaScript para mostrar el contenido
principal.

### CA-28. Persistencia y migraciones

**Dado** que se configura una instalación nueva  
**Cuando** se ejecutan las migraciones de Django  
**Entonces** se crean las estructuras necesarias para artículos y
presentación del autor  
**Y** el contenido puede persistirse y recuperarse mediante los modelos.

### CA-29. Respuestas de error

**Dado** que un visitante solicita un artículo con una ruta inválida  
**Cuando** Django procesa la solicitud  
**Entonces** devuelve HTTP 404  
**Y** la respuesta informa de que el recurso no se ha encontrado  
**Y** no presenta una página de artículo válida como sustitución silenciosa.

### CA-30. Base de datos inicial

**Dado** el entorno de desarrollo de la primera versión  
**Entonces** la aplicación puede utilizar SQLite como base de datos inicial  
**Y** la solución no presupone una base de datos de producción concreta.

## 8. Criterios de exclusión

La entrega no se considerará incompleta por no incluir:

- cuentas o perfiles de lectores;
- comentarios;
- suscripciones, boletines o notificaciones;
- buscador;
- funciones sociales, reacciones o valoraciones;
- programación o revisión editorial;
- múltiples roles editoriales;
- API pública;
- aplicación móvil nativa;
- analítica avanzada;
- internacionalización;
- selección definitiva de infraestructura o base de datos de producción.

Estas capacidades están fuera del alcance de la primera versión y no deben
introducirse como condición para aceptar la entrega.

## 9. Escenarios de aceptación de extremo a extremo

### E2E-01. Descubrir y leer un artículo

1. Un visitante accede a `/`.
2. Identifica un artículo publicado por su título, fecha y extracto.
3. Selecciona el enlace del artículo.
4. Comprueba que se muestran título, fecha, autoría y contenido completo.
5. Utiliza el enlace de regreso y vuelve a la portada.

**Resultado esperado:** el visitante puede descubrir y leer el artículo sin
obstáculos ni pasos de autenticación.

### E2E-02. Consultar la presentación del autor

1. Un visitante accede a la portada.
2. Localiza el enlace «Sobre mí» en la navegación.
3. Accede a `/sobre-mi/`.
4. Lee la presentación del autor.

**Resultado esperado:** la presentación es localizable y accesible desde la
navegación principal.

### E2E-03. Publicar y retirar contenido

1. El editor inicia sesión en Django Admin.
2. Crea un artículo con todos los campos mínimos.
3. Lo guarda como no publicado y comprueba que no aparece públicamente.
4. Lo marca como publicado y comprueba que aparece en la portada.
5. Lo retira y comprueba que deja de aparecer y no puede abrirse como
   contenido público.

**Resultado esperado:** el editor controla el ciclo básico de disponibilidad
pública sin editar plantillas.

### E2E-04. Actualizar «Sobre mí»

1. El editor inicia sesión en Django Admin.
2. Modifica el texto de presentación.
3. Guarda los cambios.
4. Un visitante accede a `/sobre-mi/`.

**Resultado esperado:** la página muestra la presentación actualizada.

## 10. Condición de aceptación de la versión

La primera versión se considerará aceptada cuando todos los criterios
aplicables de las secciones 3 a 7 se cumplan y los escenarios E2E-01 a E2E-04
puedan completarse correctamente. Los criterios de exclusión no constituyen
defectos ni requisitos pendientes de esta entrega.

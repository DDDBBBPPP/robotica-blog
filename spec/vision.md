## Visión del producto

Crear un blog de robótica sencillo, claro y centrado en la lectura, donde las
personas interesadas puedan descubrir artículos, leerlos cómodamente en
cualquier dispositivo y conocer a la persona que los escribe.

## Propósito

El sitio debe facilitar la publicación y consulta de contenidos sobre
robótica sin convertir la experiencia en una red social ni exigir
interacciones innecesarias. El editor podrá mantener los artículos y la
presentación del autor desde el panel administrativo de Django, sin tener que
modificar las plantillas del sitio.

## Usuarios principales

### Visitante

Busca información sobre robótica y necesita:

- encontrar rápidamente los artículos recientes;
- identificar el título, la fecha y el extracto de cada artículo;
- leer el artículo completo con una estructura clara de párrafos y
  subtítulos;
- volver fácilmente a la portada y consultar «Sobre mí».

### Editor del sitio

Necesita:

- crear, editar y retirar artículos;
- controlar qué artículos están publicados;
- actualizar el texto de presentación del autor;
- realizar estas tareas desde el panel administrativo estándar de Django,
  reservado a usuarios autorizados.

## Experiencia que queremos ofrecer

La portada debe servir como punto de entrada inmediato: mostrar el nombre del
blog y los artículos publicados más recientes, ordenados del más nuevo al más
antiguo. Cada artículo debe poder abrirse desde su listado y leerse en una
página propia con su título, autoría, fecha y contenido.

La navegación principal debe ser visible y comprensible, con enlaces a la
portada y a «Sobre mí». Desde un artículo, la persona lectora debe poder
regresar a la portada sin depender de JavaScript. Si no existen artículos
publicados, la portada debe explicar la situación en lugar de mostrar una
lista vacía sin contexto.

## Principios de diseño

1. **Contenido primero:** evitar elementos que distraigan de la lectura.
2. **Claridad:** usar etiquetas, títulos y enlaces descriptivos en español.
3. **Lectura cómoda:** cuidar la tipografía, el contraste, el espaciado y la
   longitud de línea.
4. **Adaptabilidad:** mantener el contenido y la navegación utilizables en
   móviles y ordenadores, sin desplazamiento horizontal innecesario.
5. **Accesibilidad:** emplear HTML semántico, una jerarquía de encabezados
   coherente y controles utilizables con teclado.
6. **Simplicidad técnica:** renderizar las páginas en el servidor con Django y
   usar JavaScript únicamente cuando exista una necesidad concreta.
7. **Separación editorial:** mostrar públicamente solo artículos publicados y
   proteger las operaciones de edición para usuarios autorizados.

## Resultado esperado

El producto tendrá éxito cuando:

- una persona pueda llegar desde la portada a un artículo y leerlo completo;
- pueda localizar y consultar «Sobre mí» desde cualquier página principal;
- la experiencia conserve su contenido y navegación en pantallas pequeñas y
  grandes;
- el editor pueda sustituir o retirar el contenido de ejemplo y actualizar la
  presentación del autor desde Django Admin, sin editar las plantillas;
- los borradores y las rutas de artículos inexistentes no expongan contenido
  público incorrectamente.
## Código de la aplicación

El código Django del blog vive en esta carpeta. La documentación del producto
se mantiene en la raíz del repositorio, separada de la aplicación.

### Estructura

- `manage.py`: punto de entrada para los comandos de Django.
- `config/`: configuración del proyecto, URLs y servidores WSGI/ASGI.
- `blog/`: modelos, vistas, administración, migraciones y pruebas del blog.

### Comandos habituales

Ejecuta estos comandos desde la raíz del repositorio con el entorno virtual
activado:

```powershell
python src/manage.py check
python src/manage.py migrate
python src/manage.py runserver
python src/manage.py test blog
```

El archivo SQLite de desarrollo, los archivos estáticos generados y los
medios subidos se excluyen del control de versiones mediante el `.gitignore`
de la raíz. Las migraciones incluyen un artículo y una presentación de ejemplo
que pueden sustituirse desde Django Admin.

### Rutas principales

- `/`: portada con artículos publicados.
- `/sobre-mi/`: presentación editable del autor.
- `/articulos/<slug>/`: detalle de un artículo publicado.
- `/admin/`: administración restringida para artículos y «Sobre mí».
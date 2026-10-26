# Blog de robótica

Aplicación web Django para publicar y consultar artículos sobre robótica. Las
personas visitantes solo pueden leer artículos publicados y la gestión del
contenido se realiza desde Django Admin por usuarios autorizados.

## Requisitos

- Windows 10 o posterior.
- [uv](https://docs.astral.sh/uv/) instalado.
- Python 3.13. El archivo `.python-version` permite que uv seleccione esta
  versión automáticamente.

La dependencia de Django está fijada en la versión 5.2.18 para que las
instalaciones sean reproducibles.

## Estructura

```text
blog/
├── PRD.md, briefing.md       # Requisitos y contexto del producto
├── spec/                      # Alcance, visión y criterios de aceptación
├── src/
│   ├── manage.py              # Comandos de Django
│   ├── config/                # Configuración, URLs y servidores
│   └── blog/                  # Modelos, vistas, Admin, migraciones y tests
├── templates/                 # Plantillas HTML
├── static/                    # CSS
├── pyproject.toml             # Proyecto y dependencias de uv
└── requirements.txt           # Alternativa compatible con pip
```

La base de datos SQLite local (`src\db.sqlite3`), el entorno virtual y los
archivos generados están excluidos de Git.

## Instalación en Windows con uv

Abre PowerShell en la raíz del repositorio:

```powershell
uv python install 3.13
uv venv --python 3.13
.\.venv\Scripts\Activate.ps1
uv sync
```

Si PowerShell impide activar scripts, puede ejecutarse el entorno sin
activarlo usando `uv run`:

```powershell
uv run python src\manage.py migrate
uv run python src\manage.py runserver
```

Como alternativa, con el entorno activado:

```powershell
python -m pip install -r requirements.txt
```

## Base de datos y usuario administrador

Ejecuta las migraciones desde la raíz:

```powershell
uv run python src\manage.py migrate
```

Crea el usuario administrador:

```powershell
uv run python src\manage.py createsuperuser
```

Si necesitas restablecer su contraseña:

```powershell
uv run python src\manage.py changepassword NOMBRE_DE_USUARIO
```

## Configuración local y producción

Por defecto, el proyecto funciona en desarrollo con `DEBUG` activado y los
hosts locales permitidos. Para un entorno no local, define variables de
entorno antes de arrancar:

```powershell
$env:DJANGO_DEBUG = "false"
$env:DJANGO_SECRET_KEY = "genera-una-clave-larga-y-aleatoria"
$env:DJANGO_ALLOWED_HOSTS = "midominio.example,www.midominio.example"
```

Nunca publiques una clave real en el repositorio. Si `DJANGO_DEBUG` es
`false`, `DJANGO_SECRET_KEY` es obligatoria.

## Arrancar el servidor

```powershell
uv run python src\manage.py runserver
```

Abre las siguientes URLs:

- Sitio público: <http://127.0.0.1:8000/>
- Sobre mí: <http://127.0.0.1:8000/sobre-mi/>
- Artículos: <http://127.0.0.1:8000/articulos/SLUG/>
- Administración: <http://127.0.0.1:8000/admin/>

## Comprobaciones

```powershell
uv run python src\manage.py check
uv run python src\manage.py test blog
```

Los borradores tienen `is_published=False` por defecto y no son accesibles
desde las URLs públicas, aunque se conozca su slug.

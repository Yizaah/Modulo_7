# Mi Tienda (Django)

Pequeña guía para ejecutar la aplicación localmente en Windows.

Requisitos previos
- Python 3.10+ instalado
- Opcional: MySQL si quieres usar la configuración por defecto (las instrucciones también incluyen alternativa con SQLite)

1) Abrir PowerShell en la carpeta del proyecto
```powershell
cd mi_tienda
```

2) Crear y activar un entorno virtual
```powershell
python -m venv venv
# PowerShell (ExecutionPolicy puede requerir cambiar a RemoteSigned)
venv\Scripts\Activate.ps1
# O en cmd
venv\Scripts\activate.bat
```

3) Instalar dependencias
```powershell
pip install -r requirements.txt
```

4) Configurar la base de datos
- Opción A — usar la configuración por defecto (MySQL):
  - Asegúrate de tener MySQL en el equipo y crear la base de datos `mi_tienda_db`.
  - Actualiza `mi_tienda/mi_tienda/settings.py` con credenciales correctas si es necesario.

- Opción B — usar SQLite para pruebas rápidas (recomendado en desarrollo):
  - Abre `mi_tienda/mi_tienda/settings.py` y reemplaza la configuración `DATABASES` por:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
  - Guardar archivo.

5) Aplicar migraciones
```powershell
python manage.py migrate
```

6) (Opcional) Cargar datos iniciales
```powershell
python manage.py loaddata productos/fixtures/datos_iniciales.json
```

7) Crear superusuario (para acceder a `/admin/`)
```powershell
python manage.py createsuperuser
```

8) Ejecutar servidor de desarrollo
```powershell
python manage.py runserver
```

9) URLs útiles
- Página de inicio: http://127.0.0.1:8000/
- Productos: http://127.0.0.1:8000/productos/
- Admin: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/accounts/login/

Notas de seguridad y despliegue
- `DEBUG = True` está configurado actualmente en `settings.py`. Antes de desplegar, establece `DEBUG = False`, configura `ALLOWED_HOSTS` y asegúrate de gestionar `SECRET_KEY` mediante variables de entorno.
- Si habilitas HTTPS en producción, activa `SESSION_COOKIE_SECURE = True` y `CSRF_COOKIE_SECURE = True`.


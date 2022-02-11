
### Exit from database
```shell
exit
```

Django
----
Create `static files in weather app`
```
     weater/static/notes/css
     weater/static/notes/img
     weater/static/notes/js
```
Create `templates in weather app`
```
     weather/templates/notes
```

Edit `settings.py`
```python
STATICFILES_DIRS = []

STATIC_ROOT = BASE_DIR / "staticfiles" / "static"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "staticfiles" / "media"
MEDIA_URL = "/media/"
```



Edit `settings.py`
```python
import os
...
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('DB_NAME'),
        "USER": os.getenv('DB_USER'),
        "PASSWORD": os.getenv('DB_PASSWORD'),
        "HOST": os.getenv('DB_HOST', 'localhost'),
        "PORT": os.getenv('DB_PORT', 5432),
    }
}
```

### collect assets 
```shell
python manage.py collectstatic
```

...

# Docker


```shell
docker system prune -a
```

```shell
docker-compose build --no-cache
```

```shell
docker-compose up -d --force-recreate
```

```shell
docker-compose exec app ./manage.py migrate
```
```shell
docker-compose exec app ./manage.py makemigrations
```
```shell
docker-compose exec app ./manage.py migrate
```

```shell
docker-compose exec app ./manage.py createsuperuser
```




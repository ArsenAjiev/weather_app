
# Weather_app

### Create directory and .gitignore file
```shell
### Create weather_app directory
     mkdir weather_app
     
     cd weather_app/

### Venv
   
```shell
# Create environment
python3.8 -m venv --copies venv

# Activate
source venv/bin/activate

# Make sure to use venv/bin/pip3.8 
which pip3.8

```


### Install packages
```shell
pip install Django==4.0.2

pip install psycopg2-binary==2.9.3

pip install requests==2.27.1
```

### Create and install requirements.txt, if necessary.
      
```shell
pip freeze > requirements.txt

pip install -r requirements.txt
```



### Create Django project in weather_app directory
```shell
django-admin startproject app

python manage.py startapp weather
```



PostgreSQL
----
### Create database and user using docker-compose file
### If in docker-compose file says:
___________________________________________________
```shell      services:
        db:
          image: postgres
          environment:
            - POSTGRES_PASSWORD=pass
            - POSTGRES_DB=custom_db
            - POSTGRES_USER=custom_user
          ports:
            - 5432:5432
```

### Use script to login to the database

```shell
      psql -U custom_user -h localhost custom_db
```
          enter password

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




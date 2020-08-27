
### `CRUD operations for employee:`
get:    http://localhost:8000/api/employee/
create: http://localhost:8000/api/employee/
update: http://localhost:8000/api/employee/{id}/
delete: http://localhost:8000/api/employee/{id}/

#### `CRUD operations for manager:`
get:    http://localhost:8000/api/manager/ <br />
create: http://localhost:8000/api/manager/ <br />
update: http://localhost:8000/api/manager/{id}/ <br />
delete: http://localhost:8000/api/manager/{id}/ <br />


#### `requirements:`
Django==3.1 <br />
Python==3.6.9  <br />
django-cors-headers==3.5.0  <br />
djangorestframework==3.11.1  <br />
psycopg2-binary==2.8.5 (if using db postgreSQL. it is a postgreSQL adapter which is used to connect with python.) <br />

#### `Set Database configurations in Setting.py`
DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'PASSWORD': '',
        'USER': '',
        'HOST': '',
    }
}

### `step1: to create tables in Data base`
python manage.py migrate 

### `step2: to runserver`
python manage.py runserver

### `To create super user`
python manage.py createsuperuser
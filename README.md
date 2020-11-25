# ToDoApplication
This is just simple todo application in which we can perform crud operations on frontend.

# Technology Required
1. python3
2. Django 3

# Project Structure
```.
├── app
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── static
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── Todoweb
    ├── __init__.py
    ├── __pycache__
    ├── settings.py
    ├── urls.py
    └── wsgi.py



```
# Setup

Apply the database migrations:

```
python3 manage.py migrate
```  
Create administrator/super user:
```
python3 manage.py createsuperuser 
```

Finally, run the development server:

```
python3 manage.py runserver
```
The site will be available at 127.0.0.1:8000. `

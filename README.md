# Sparktake Blog
This is a blog developed with Django

## 1. Install

1. Create new virtual environment with python 3.5 and start the virtual environment

```
python -m venv ./.venv
.\.venv\Scripts\activate
```

2. Install dependencies

```
pip install django-crispy-forms==1.9
pip install django-registration==2.3
pip install django-markdown-deux==1.0.5
pip install django-pagedown==1.0.5
pip install djangorestframework==3.7.7
pip install djangorestframework-jwt
```

3. Uninstall the Django that is installed along the dependecies and get Django 1.11

```
pip uninstall django
pip install django==1.11
```

## 2. Start Server

1. Start MongoDB

```
mongod
```

2. Run the server

```
python manage.py runserver
```

## 3. Exit

1. Exit virtual environment

```
deactivate
```

*Due to the shutdown of this project, the AWS bucket used to stored the avatars and post images is removed, therefore some functions may not worked.
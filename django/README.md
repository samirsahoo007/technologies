# :scroll: Django Cheat Sheet

## Sections
- :snake: [Initializing pipenv](#snake-initializing-pipenv-optional) (optional)
- :blue_book: [Creating a project](#blue_book-creating-a-project)
- :page_with_curl: [Creating an app](#page_with_curl-creating-an-app)
- :tv: [Creating a view](#tv-creating-a-view)
- :art: [Creating a template](#art-creating-a-template)
- :ticket: [Creating a model](#ticket-creating-a-model)
- :postbox: [Creating model objects and queries](#postbox-creating-model-objects-and-queries)
- :man: [Using the Admin page](#man-using-the-admin-page)


## :snake: Initializing pipenv (optional)
- `pip install virtualenv`
- `virtualenv -p python2.7 <desired-path>`
- `source <desired-path>/bin/activate`
- `pip3 install django==2.0.3`

## :blue_book: Creating a project
- `django-admin startproject <project_name>`

The project directory should look like this:
```
<project_name>/
    manage.py
    <project_name>/
        __init__.py
        settings.py
        urls.py							# In this file, we can mention the URLs and corresponding actions to perform the task and display the view.
        wsgi.py							# It is an entry-point for WSGI-compatible web servers to serve Django project.
```
- `$ python manage.py runserver` 				(or python manage.py runserver 8080)

- The admin app (django.contrib.admin) is enabled by default and already added into INSTALLED_APPS section of the settings file => localhost:8000/admin/

## :page_with_curl: Database setup
project/settings.py

- By default, the configuration uses SQLite. We can also use 'django.db.backends.mysql', or 'django.db.backends.oracle' for mysql and oracle in settings.py.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
```

e.g.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

- `python manage.py migrate`					# This command will create tables for admin, auth, contenttypes, and sessions.

## :page_with_curl: Creating an app
- `$ python manage.py startapp <app_name>`
- Inside the `app` folder, create a file called `urls.py`

The project directory should now look like this:
```
project/
    manage.py
    db.sqlite3
    project/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    app/
        migrations/						# migrations folder to store migration files and model to write business logic.
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        urls.py
        views.py
```

## Register / Use Model
- To include this app in your project, add your app to the project's `settings.py` file by adding its name to the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
	'app',
	# ...
]

- By default
INSTALLED_APPS = [
    'django.contrib.admin',			# The admin site.
    'django.contrib.auth',			# An authentication system
    'django.contrib.contenttypes',		# A framework for content types.
    'django.contrib.sessions',			# A session framework.
    'django.contrib.messages',			# A messaging framework.
    'django.contrib.staticfiles',		# A framework for managing static files.
]

```
- To migrate changes over:
```bash
$ python manage.py migrate
```
## :ticket: Migrating Model

Each Django's model is mapped to a table in the database. So after creating a model, we need to migrate it. Let's see an example.

Suppose, we have a model class Employee in the models.py file that contains the following code.

```python
from django.db import models  
class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    class Meta:  
        db_table = "employee"  
```
```bash
$ python3 manage.py makemigrations 				# Django first creates a migration file that contains the details of table structure. 
$ python3 manage.py migrate					# Now, migrate to reflect the changes into the database.
```

This model will create a table into the database that looks like below.
CREATE TABLE appname_employee (  
    "id" INT NOT NULL PRIMARY KEY,  
    "first_name" varchar(30) NOT NULL,  
    "last_name" varchar(30) NOT NULL  
);  


## :tv: Creating a view
- Within the app directory, open `views.py` and add the following:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")
```
- Still within the app directory, open (or create)  `urls.py` 
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
- Now within the project directory, edit `urls.py` to include the following
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),
]
```
- To create a url pattern to the index of the site, use the following urlpattern:
```python
urlpatterns = [
    path("", include('app.urls')),
]
```
- Remember: there are multiple files named `urls.py`
- The `urls.py` file within app directories are organized by the `urls.py` found in the project folder.

## :art: Django Static Files Handling
In a web application, apart from business logic and data handling, we also need to handle and manage static resources like CSS, JavaScript, images etc.

It is important to manage these resources so that it does not affect our application performance.

1. Include the django.contrib.staticfiles in INSTALLED_APPS.

```python
INSTALLED_APPS = [  
    'django.contrib.admin',  
    'django.contrib.auth',  
    'django.contrib.contenttypes',  
    'django.contrib.sessions',  
    'django.contrib.messages',  
    'django.contrib.staticfiles',  
    'myapp'  
]  
```

2. Define STATIC_URL in settings.py

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static")
]
```
3. {% load static %}   						# Load static files in the templates
4. Store all images, JavaScript, CSS files in a static folder of the application. First create a directory static, store the files inside it.

e.g.
```python
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Index</title>  
     {% load static %}  
    <script src="{% static '/js/script.js' %}" type="text/javascript"></script>  
</head>  
<body>  
</body>  
</html>  
```

## :art: Creating a template
- Within the app directory, HTML, CSS, and JavaScript files are located within the following locations:
```
app/
   templates/
      index.html
   static/
      style.css
      script.js
```
- To add a template to views, open `views.py` within the app directory and include the following:
```python
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
```
- To include context to the template:
```python
def index(request):
	context = {"context_variable": context_variable}
    return render(request,'index.html', context)
```
- Within the HTML file, you can reference static files by adding the following:
```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		
		<link rel="stylesheet" href="{% static 'styles.css' %}">
	</head>
</html>
```
- To add an `extends`:
```html
{% extends 'base.html'% }

{% block content %}

Hello, World!

{% endblock %}
```
- And then in `base.html` add:
```html
<body>
	{% block content %}{% endblock %}
</body>
```

- In HTML, a form is a collection of elements inside <form>...</form> that allow a visitor to do things like enter text, select options, checkbox, 
## :man: Django Model Form

It is a class which is used to create an HTML form by using the Model. It is an efficient way to create a form without writing HTML code.

Django automatically does it for us to reduce the application development time. For example, suppose we have a model containing various fields, we don't need to repeat the fields in the form file.

```python
from django import forms  
from myapp.models import Employee 
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Employee 
        fields = "__all__"  
```
- Refer above for views.py and urls.py
- index.html
```python
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Index</title>  
</head>  
<body>  
<form method="POST" class="post-form">  
        {% csrf_token %}  
        {{ form.as_p }}  
        <button type="submit" class="save btn btn-default">Save</button>  
    </form>  
</body>  
</html>  
```

## :man: Django Forms

It is similar to the ModelForm class that creates a form by using the Model, but it does not require the Model. So instantiation in views.py in django forms and model forms as below respectively

from myapp.form import EmployeeForm
from myapp.models import EmployeeForm

Each field of the form class map to the HTML form <input> element and each one is a class itself, it manages form data and performs validation while submitting the form.

```python
from django import forms  
class EmployeeForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)  
```

- urls.py and index.html is similar as in ModelForms

## :man: Create an Admin User

- `python managen.py createsuperuser`

############### Read more aboout models here #################
## :ticket: Creating a model
- Within the app's `models.py` file, an example of a simple model can be added with the following:
```python
from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
```
*Note that you don't need to create a primary key, Django automatically adds an IntegerField.*

- To inact changes in your models, use the following commands in your shell:
```
$ python manage.py makemigrations <app_name>
$ python manage.py migrate
```
*Note: including <app_name> is optional.*
- A one-to-many relationship can be made with a `ForeignKey`:
```python
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```
- In this example, to query for the set of albums of a musician:
```python
>>> m = Musician.objects.get(pk=1)
>>> a = m.album_set.get()
```
 
- A many-to-many relationship can be made with a `ManyToManyField`:
```python
class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```
*Note that the `ManyToManyField`  is **only defined in one model**. It doesn't matter which model has the field, but if in doubt, it should be in the model that will be interacted with in a form.*

- Although Django provides a `OneToOneField` relation, a one-to-one relationship can also be defined by adding the kwarg of `unique = True` to a model's `ForeignKey`:
```python
ForeignKey(SomeModel, unique=True)
```
	
- For more detail, the [official documentation for database models]( https://docs.djangoproject.com/en/2.0/topics/db/models/) provides a lot of useful information and examples.

## :postbox: Creating model objects and queries
- Example `models.py` file:
```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
```
- To create an object within the shell or to play with the API:
```
$ python manage.py shell
```
```python
>>> from blog.models import Blog
>>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
>>> b.save()
```
- To save a change in an object:
```python
>>> b.name = 'The Best Beatles Blog'
>>> b.save()
```
- To retrieve objects:
```python
>>> all_entries = Entry.objects.all()
>>> indexed_entry = Entry.objects.get(pk=1)
>>> find_entry = Entry.objects.filter(name='Beatles Blog')
```

Ref: https://www.javatpoint.com/django-database-migrations


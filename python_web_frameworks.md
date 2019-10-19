# Top Python Web Frameworks

| Project Name | Stars | Forks | Description |Templates	| Forms	| ORM |
| ------------ | ----- | ----- | ----------- |----------|-------|-----|
| [flask](https://github.com/pallets/flask) | 43463 | 12243 | The Python micro framework for building web applications. | Jinja | WTForms | [SQLAlchemy](http://www.fullstackpython.com/object-relational-mappers-orms.html) |
| [django](https://github.com/django/django) | 40999 | 17643 | The Web framework for perfectionists with deadlines. | default | default | [Django ORM](https://www.fullstackpython.com/object-relational-mappers-orms.html) |
| [tornado](https://github.com/tornadoweb/tornado) | 17617 | 4906 | Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. | _ | _ | _ |
| [pyramid](https://github.com/Pylons/pyramid) | 3104 | 851 | Pyramid - A Python web framework | _ | _ | _ |
| [web2py](https://github.com/web2py/web2py) | 1749 | 810 | Free and open source full-stack enterprise framework for agile development of secure database-driven web-based applications, written and programmable in Python. | _ | _ | _ |

Other frameworks: sanic, dash, aiohttp, falcon, bottle, hug, vibora, cherrypy, masonite, Growler, morepath, tg2, circuits

# Full-stack web frameworks

## Django

Django is one of the most popular Python frameworks. It offers a lot of out-of-the-box functionalities like Admin Panel or Generic Views and Forms. Django’s main characteristics are:

* one managing script (“manage.py”) that can be used for performing most of the framework specific actions (like starting the development server, creating an admin user, collecting static files etc.),

* synchronous request processing,

* MTV (model-template-view) architecture pattern (which is variation of the model-view-controller pattern),

* custom object-relational mapping  (ORM) for communicating with the database,

* Django is strict and forces its own coding style on the developer – a lot of meta programming,

* custom HTML templates rendering engine,

* custom URL routing system,

* support for static files - URL routing as well as detection and collection,

* a large number of external modules, e.g. Django REST Framework, Django CMS, Django Channels (websockets).


Django is a good fit for bigger projects, 

Other Fullstack frameworks: Web2py, TurboGears
# Microframeworks

## Flask

It’s one of the most popular Python microframeworks, it’s reliable and fast.  The main characteristics of the framework are:

* synchronous request support,

* doesn’t force any project architecture, but has some recommendations (package, module, blueprints),

* it doesn’t offer ORM, but SQLAlchemy or other can be used,

* supports functions as well as some Django-like generic class views (starting from Flask 0.7),

* loose coding style, it doesn’t force any solutions, most decisions are left to the developer’s discretion,

* it’s possible to use Jinja2 HTML Template engine,

* Werkzeug routing system,

* supports basic static file routing,


can be extended with some additional third-party modules, e.g. Flask-RESTful for REST API creation or flask-socketio for Web Sockets Support.

This framework will do the trick in small and medium projects. It has some third-party modules that are ready to be used as well as good native solutions. Flask should prove itself in jobs where complicated custom features are required but Django seems too big for the task. On the other hand, setting Flask for a bigger project from the beginning can be tricky as there is no “official” way of doing so.

Common:
* compliant with the WSGI standard,

Other microframeworks: Pyramid,  CherryPy, BottlePy
# Asynchronous frameworks

## Tornado

Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed (a social aggregation site). Thanks to that, it offers a built-in integration with social services such as Google, Facebook, and Twitter. The integration with other frameworks and libraries is also possible: Twisted, asyncio or even WSGI applications. Tornado’s features:

* offers a lot of generic classes that can be used for creating the application, e.g. Router, or SocketHandler for websockets,

* custom HTML template engine,

* custom routing handling – offers generic classes than can be used for route creation,

* it supports WSGI, but it’s not recommended – the user should use Tornado’s own interfaces instead,

* out-of-the-box websockets support, authentication (e.g. via Google), and security features (like cookie signing or XSRF protection),

* no additional tools are needed for REST API creation.

The framework should work well in cases where there are a lot of incoming connections that can be handled quickly or in real-time solutions, e.g. chats. Tornado tries to solve the c10k problem so high processing speed is a priority. Another advantage of Tornado is its native support for social services. This framework won’t be a good choice for creating standard CRUD sites or big business applications, as it wasn’t designed to be used that way. For bigger projects, it can be integrated with WSGI applications as a part of their bigger structure and take care of tasks that require high handling speeds.

Other asynchronous frameworks: Aiohttp, Sanic, Twist

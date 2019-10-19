# Top Python Web Frameworks

| Project Name | Stars | Forks | Description |Templates	| Forms	| ORM |
| ------------ | ----- | ----- | ----------- |----------|-------|-----|
| [flask](https://github.com/pallets/flask) | 43463 | 12243 | The Python micro framework for building web applications. | Jinja | WTForms | [SQLAlchemy](http://www.fullstackpython.com/object-relational-mappers-orms.html) |
| [django](https://github.com/django/django) | 40999 | 17643 | The Web framework for perfectionists with deadlines. | default | default | [Django ORM](https://www.fullstackpython.com/object-relational-mappers-orms.html) |
| [tornado](https://github.com/tornadoweb/tornado) | 17617 | 4906 | Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. | _ | _ |[tornado-sqlalchemy](https://tornado-sqlalchemy.readthedocs.io/en/latest/)|
| [pyramid](https://github.com/Pylons/pyramid) | 3104 | 851 | Pyramid - A Python web framework | _ | _ | _ |
| [web2py](https://github.com/web2py/web2py) | 1749 | 810 | Free and open source full-stack enterprise framework for agile development of secure database-driven web-based applications, written and programmable in Python. | _ | _ | _ |

Other frameworks: sanic, dash, aiohttp, falcon, bottle, hug, vibora, cherrypy, masonite, Growler, morepath, tg2, circuits

Flask: Meant for small, simple projects; makes it easy for us to construct views and connect them to routes quickly; can be encapsulated in a single file without much fuss
Pyramid: Meant for mid sized; contains a fair bit of configuration to get up and running; separate realms of application components can easily be divided and built out to arbitrary depth without losing sight of the central application
Tornado: Meant for projects benefiting from precise and deliberate I/O control; allows for co-routines and easily exposes methods that can control how requests are received/responses are sent and when those operations occur
Django: meant for big things that may get bigger; large ecosystem of add-ons and mods; very opinionated in its configuration and management in order to keep all the disparate parts in line

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

* loose coding style, it doesn't force any solutions, most decisions are left to the developer’s discretion,

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
Tornado is good for handling a lot of connections, since it can respond to an incoming client, dispatch a request handler and don't think about that client until the result-callback is pushed on the event queue. So for that specific quality Tornado should be used when you want to scale well when handling a lot of requests. The async processing facilitates functional decoupling and shared-nothing data access. That swings really well with stateless design like REST or other Service Oriented Architectures. You also don't have to deal with spawning threads or processes with the inherent overhead so much and you can save some of the locking/IPC trouble.

* offers a lot of generic classes that can be used for creating the application, e.g. Router, or SocketHandler for websockets,

* custom HTML template engine,

* custom routing handling – offers generic classes than can be used for route creation,

* it supports WSGI, but it’s not recommended – the user should use Tornado’s own interfaces instead,

* out-of-the-box websockets support, authentication (e.g. via Google), and security features (like cookie signing or XSRF protection),

* no additional tools are needed for REST API creation.

The framework should work well in cases where there are a lot of incoming connections that can be handled quickly or in real-time solutions, e.g. chats. Tornado tries to solve the c10k problem so high processing speed is a priority. Another advantage of Tornado is its native support for social services. This framework won’t be a good choice for creating standard CRUD sites or big business applications, as it wasn’t designed to be used that way. For bigger projects, it can be integrated with WSGI applications as a part of their bigger structure and take care of tasks that require high handling speeds.

Other asynchronous frameworks: Aiohttp, Sanic, Twist

### Important notes:

* @coroutine:
The first major piece here is the @coroutine decorator, imported from tornado.gen. Any Python callable that has a portion that acts out of sync with the normal flow of the call stack is effectively a "co-routine"; a routine that can run alongside other routines. In the example of my household chores, pretty much every chore was a co-routine. Some were blocking routines (e.g., vacuuming the floor), but that routine simply blocked my ability to start or attend to anything else. It didn't block any of the other routines that were already set in motion from continuing.

Tornado offers a number of ways to build an app that take advantage of co-routines, including allowing us to set locks on function calls, conditions for synchronizing asynchronous routines, and a system for manually modifying the events that control the I/O loop.

The only way the @coroutine decorator is used here is to allow the get method to farm out the SQL query as a background process and resume once the query is complete, while not blocking the Tornado I/O loop from handling other sources of incoming data. That is all that's "asynchronous" about this implementation: out-of-band database queries. Clearly if we wanted to showcase the magic and wonder of an async web app, a To-Do List isn't the way.

* tornado-sqlalchemy:
Why use this instead of just the bare SQLAlchemy? Well, tornado-sqlalchemy has all the goodness of straightforward SQLAlchemy, so we can still declare models with a common Base as well as use all the column data types and relationships to which we've grown accustomed. Alongside what we already know from habit, tornado-sqlalchemy provides an accessible async pattern for its database-querying functionality specifically to work with Tornado's existing I/O loop.

The tornado-sqlalchemy package provides us with the as_future function. The job of as_future is to wrap the query constructed by the tornado-sqlalchemy session and yield its return value. If the view method is decorated with @coroutine, then using this yield as_future(query) pattern will now make your wrapped query an asynchronous background process. The I/O loop takes over, awaiting the return value of the query and the resolution of the future object created by as_future.

To have access to the result from as_future(query), you must yield from it. Otherwise, you get only an unresolved generator object and can do nothing with the query.

 When Tornado (as of v.4.5) consumes data from a client and organizes it for use in the application, it keeps all the incoming data as bytestrings. However, all the code here assumes Python 3, so the only strings that we want to work with are Unicode strings. We can add another method to this BaseView class whose job it will be to convert the incoming data to Unicode before using it anywhere else in the view.

* class based views:
Unlike the function-based views we've seen in the Flask and Pyramid implementations, Tornado's views are all class-based. This means we'll no longer use individual, standalone functions to dictate how requests are handled. Instead, the incoming HTTP request will be caught and assigned to be an attribute of our defined class. Its methods will then handle the corresponding request types.

## The basics of async in Python and the I/O loop

Due to the global interpreter lock (GIL), Python is—by design—a single-threaded language. For every task a Python program must execute, the full attention of its thread of execution is on that task for the duration of that task. Our HTTP server is written in Python. Thus, when data (e.g., an HTTP request) is received, the server's sole focus is that incoming data. This means that, in most cases, whatever procedures need to run in handling and processing that data will completely consume your server's thread of execution, blocking other potential data from being received until your server finishes whatever it needed to do.

In many cases this isn't too problematic; a typical web request-response cycle will take only fractions of a second. Along with that, the sockets that HTTP servers are built from can maintain a backlog of incoming requests to be handled. So, if a request comes in while that socket is handling something else, chances are it'll just wait in line a bit before being addressed. For a low to intermediate traffic site, a fraction of a second isn't that big of a deal, and you can use multiple deployed instances along with a load-balancer like NGINX to distribute traffic for the larger request loads.

What if, however, your average response time takes more than a fraction of a second? What if you use data from the incoming request to start some long-running process like a machine-learning algorithm or some massive database query? Now, your single-threaded web server starts to accumulate an unaddressable backlog of requests, some of which will get dropped due to simply timing out. This is not an option, especially if you want your service to be seen as reliable on a regular basis.

In comes the asynchronous Python program. It's important to keep in mind that because it's written in Python, the program is still a single-threaded process. Anything that would block execution in a synchronous program, unless specifically flagged, will still block execution in an asynchronous one.
When it's structured correctly, however, your asynchronous Python program can "shelve" long-running tasks whenever you designate that a certain function should have the ability to do so. Your async controller can then be alerted when the shelved tasks are complete and ready to resume, managing their execution only when needed without completely blocking the handling of new input.

That was somewhat jargony, so let's demonstrate with a human example.

### Bringing it home

I often find myself trying to get multiple chores done at home with little time to do them. On a given day, that backlog of chores may look like:

Cook a meal (20 min. prep, 40 min. cook)
Wash dishes (60 min.)
Wash and dry laundry (30 min. wash, 90 min. dry per load)
Vacuum floors (30 min.)

If I were acting as a traditional, synchronous program, I'd be doing each task myself, by hand. Each task would require my full attention to complete before I could consider handling anything else, as nothing would get done without my active attention. So my sequence of execution might look like:

Focus fully on preparing and cooking the meal, including waiting around for food to just… cook (60 min.).
Transfer dirty dishes to sink (65 min. elapsed).
Wash all the dishes (125 min. elapsed).
Start laundry with my full focus on that, including waiting around for the washing machine to finish, then transferring laundry to the dryer, and waiting for the dryer to finish (250 min. elapsed).
Vacuum the floors (280 min. elapsed).

That's 4 hours and 40 minutes to complete my chores from end-to-end.

Instead of working hard, I should work smart like an asynchronous program. My home is full of machines that can do my work for me without my continuous effort. Meanwhile, I can switch my attention to what may actively need it right now.

My execution sequence might instead look like:

Load clothes into and start the washing machine (5 min.).
While the washing machine is running, prep food (25 min. elapsed).
After prepping food, start cooking food (30 min. elapsed).
While the food is cooking, move clothes from the washing machine into the dryer and start dryer (35 min. elapsed).
While dryer is running and food is still cooking, vacuum the floors (65 min. elapsed).
After vacuuming the floors, take food off the stove and load the dishwasher (70 min. elapsed).
Run the dishwasher (130 min. when done).

Now I'm down to 2 hours and 10 minutes. Even if I allow more time for switching between jobs (10-20 more minutes total), I'm still down to about half the time I would've spent if I'd waited to perform each task in sequential order. This is the power of structuring your program to be asynchronous.

So where does the I/O loop come in?

An asynchronous Python program works by taking in data from some external source (input) and, should the process require it, offloading that data to some external worker (output) for processing. When that external process finishes, the main Python program is alerted. The program then picks up the result of that external processing (input) and continues on its merry way.

Whenever that data isn't actively in the hands of the main Python program, that main program is freed to work on just about anything else. This includes awaiting completely new inputs (e.g., HTTP requests) and handling the results of long-running processes (e.g., results of machine-learning algorithms, long-running database queries). The main program, while still single-threaded, becomes event-driven, triggered into action for specific occurrences handled by the program. The main worker that listens for those events and dictates how they should be handled is the I/O loop.

This is kind of like my asynchronous chores above. When my attention is fully necessary for prepping food, that's all I'm doing. However, when I can get the stove to do work for me by cooking my food, and the dishwasher to wash my dishes, and the washing machine and dryer to handle my laundry, my attention is freed to work on other things. When I am alerted that one of my long-running tasks is finished and ready to be handled once again, if my attention is free, I can pick up the results of that task and do whatever needs to be done with it next.

# Thoughts about using the right tool for the right job

What we're starting to see as we continue to move through these web frameworks is that they can all effectively handle the same problems. For something like this To-Do List, any framework can do the job. However, some web frameworks are more appropriate for certain jobs than other ones, depending on what "more appropriate" means for you and your needs.

While Tornado is clearly capable of handling the same job that Pyramid or Flask can handle, to use it for an app like this is effectively a waste. It's like using a car to travel one block from home. Yes it can do the job of "travel," but short trips aren't why you choose to use a car over a bike or just your feet.

Per the documentation, Tornado is billed as "a Python web framework and asynchronous networking library." There are few like it in the Python web framework ecosystem. If the job you're trying to accomplish requires (or would benefit significantly from) asynchronicity in any way, shape, or form, use Tornado. If your application needs to handle multiple, long-lived connections while not sacrificing much in performance, choose Tornado. If your application is many applications in one and needs to be thread-aware for the accurate handling of data, reach for Tornado. That's where it works best.

Use your car to do "car things." Use other modes of transportation to do everything else.

Ref: https://opensource.com/article/18/6/tornado-framework


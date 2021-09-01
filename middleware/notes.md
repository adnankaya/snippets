1. What is a middleware in django
- it acts as a bridge between 2 parts of a program or the system that enables communication between them.
- in technical terms; middleware is a framework of hooks into (be connected) Django's request/response procesing.
- it is a light, low-level plugin system for globally altering django's input or output .
- each middleware component is responsible for doing some specific function.

2. How does middleware work ?
- when a user makes a request from the application a WSGI handler is instantiated which handles the following things:
    - imports project's `settings.py' and django exception classes.
    - loads all the middleware classes which are written in MIDDLEWARE tuple located in settings.py file.
    - builds list of methods which handle processing of request, view, response & exception
    - loops through the request methods in order
    - resolves the requested URL
    - loops through each of the view processing methods
    - calls the view function
    - processes exception methods (if any)
    - loops through each of the response methods in the reverse order from request middleware
    - builds a return value and makes a call to the callback function

3. What are the types of Middleware ?
There are 2 types of middleware in django 
- builtin middleware; provided by django
- custom middleware; you can write your own middleware which can be used throughout your project.
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
4. How to write a custom middleware in django ?
- create a python package (a folder with `__init__`.py) named as `middleware`
- create a file named `custom_middleware` (or anything which you like ) and a regular python function/class in it.
- you can write middleware as function or as a class whose instances are callable

Function Based Middleware
```python
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
```
Class Based Middleware
```python
class ExampleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code that is executed in each request before the view is called

        response = self.get_response(request)

        # Code that is executed in each request after the view is called
        return response

    def process_view(request, view_func, view_args, view_kwargs):
        # This code is executed just before the view is called

    def process_exception(request, exception):
        # This code is executed if an exception is raised

    def process_template_response(request, response):
        # This code is executed if the response contains a render() method
        return response

```
Now the final step will be to add your custom middleware in MIDDLEWARE List in settings.py file
```python
MIDDLEWARE = [
    …
    'your_app.middleware_directory.custom_middleware_file.CustomMiddleware_class',
]
```
Further, let’s understand the special methods of class-based middleware:

- `process_request`: The request object will be created while Django goes through process_request method in each middleware. After that, it resolves which view to be called soon after the request object is created with the help of `ROOT_URLCONF` key in `settings` file.

- `process_view(request, view_func, view_args, view_kwargs)`: request is the `HttpRequest` object and view_func is the function that is being called. It will be called just before calling the view.

- `process_response`: The response will be the final output Django will process after executing the process_response method in each middleware which will be `HttpResponse` object.

- `process_template_response(request, response)`: request is an `HttpRequest` object. response is the TemplateResponse object (or equivalent) returned by a Django view or by a middleware.
process_exception(request, exception): request is an HttpRequest object. exception is an `Exception` object raised by the view function. This method is called when the view raises an exception.

5. Things to remember when using middleware:
- Order of middleware is important
- A middleware only need to extend from class object
- A middleware is free to implement some of the methods and not implement other methods.
- A middleware may implement `process_request` but may not implement `process_response` and `process_view`


Resource:
[Medium, Akash Shrivastava](https://medium.com/scalereal/everything-you-need-to-know-about-middleware-in-django-2a3bd3853cd6)
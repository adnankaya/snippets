## Deployment Angular & Django Project to Ubuntu Server with Apache

### Ubuntu Server Requirements
- `sudo apt-get install apache2`
- `sudo apt-get install libapache2-mod-wsgi-py3`
- `sudo apt-get install virtualenv`

### Django Project
```bash
ubuntu@server virtualenv -p python3 env
ubuntu@server source env/bin/activate
(env)ubuntu@server pip install django djangorestframework django-cors-headers
(env)ubuntu@server django-admin startproject src
(env)ubuntu@server mv src backend # rename project name as backend
(env)ubuntu@server cd backend
(env)ubuntu@server ~/backend pip freeze > requirements.txt
(env)ubuntu@server ~/backend sudo apt-get install tree # to display files/folders like a tree
(env)ubuntu@server ~/backend tree .
.
├── manage.py
├── requirements.txt
└── src
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```
- **`backend/src/settings.py`**
```python
...
# Application definition

INSTALLED_APPS = [
    ...
    # External
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    # Internal Apps
    'api',
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "static" ],
        ...
    },
]
STATIC_URL = '/static/'
# Admin and Django Rest Framework
STATIC_ROOT = BASE_DIR / 'static'


# If this is used then `CORS_ORIGIN_WHITELIST` will not have any effect
CORS_ORIGIN_ALLOW_ALL = False
# If this is used, then not need to use `CORS_ORIGIN_ALLOW_ALL = True`
CORS_ORIGIN_WHITELIST = (
    "http://127.0.0.1:4200",
    "http://localhost:4200",
    "http://www.yourdomain.com"
)
ALLOWED_HOSTS = [
                'localhost', 
                '127.0.0.1',
                'yourdomain.com',
                'http://yourdomain.com/',
                'www.yourdomain.com' ]

```
- **`urls.py`**
```python
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # To handle all requested URLS/Paths we defined the following path with re_path
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html'), name="index"),
]



```

### Apache Configuration File
```bash
adnan@pc cd /etc/apache2/sites-available
adnan@pc sudo nano django-project.conf

```
- **`django-project.conf`**
```
<VirtualHost *:80>
#	ServerName localhost
#	ServerAdmin webmaster@localhost

	Alias /static /home/adnan/backend/static
	<Directory /home/adnan/backend/static>
		Require all granted
	</Directory>

	Alias /media /home/adnan/backend/media
	<Directory /home/adnan/backend/media>
		Require all granted
	</Directory>

	<Directory /home/adnan/backend/src>
        <Files wsgi.py>
            Require all granted
        </Files>
	</Directory>

	WSGIDaemonProcess yourdomain.com python-home=/home/adnan/backend/env python-path=/home/adnan/backend
	WSGIProcessGroup yourdomain.com
	WSGIScriptAlias / /home/adnan/backend/src/wsgi.py


	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

```
### Angular
- `ng build --prod --deploy-url /static/`
- **copy** files in *dist*  folder to the django project **static** folder.


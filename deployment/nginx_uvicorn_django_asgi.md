# Gunicorn Uvicorn Conf

##### `/etc/systemd/system/gunicorn.service`

```bash
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=myuser
Group=www-data
WorkingDirectory=/home/myuser/myproject

ExecStart=/home/myuser/myproject/venv/bin/gunicorn \ # pip install gunicorn must be performed
    -k uvicorn.workers.UvicornWorker \ # use uvicorn
    --capture-output --enable-stdio-inheritance \
    --workers=49 --bind unix:/run/gunicorn.sock \
    --log-level DEBUG \
    --log-file '/home/myuser/logs/gunicorn.log' \ # we can see gunicorn logs on this directory
    src.asgi:application #myproject has src folder which has settings, wsgi, asgi files


ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target

```

##### `/etc/systemd/system/gunicorn.socket`

```bash
    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/run/gunicorn.sock

    [Install]
    WantedBy=sockets.target
```

##### `/etc/nginx/sites-available/myproject`

```bash
server {

    listen 80;
    server_name 123.123.123.123; # your IP address

    location = /favicon.ico { access_log off; log_not_found off; }

    location /staticroot/ { # in django settings
        root /home/myuser/myproject;
    }


    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }    

    location /media/ {
    	root /home/myuser/myproject;
    }
}

```


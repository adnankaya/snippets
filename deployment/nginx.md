## Deployment Nginx, Gunicorn
#### Github
- Token address : https://github.com/settings/tokens
- Github CLI installation
```bash
$ curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
$ sudo apt update
$ sudo apt install gh
$ gh auth login
$ gh repo clone adnankaya/agency

```
#### Ubuntu Packages
```bash
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
sudo apt install gettext
sudo apt install virtualenv
cd agency
virtualenv -p python3 venv
source venv/bin/activate
pip install -r prod-requirements.txt
```
##### Environment Variables
```bash
cp .env.example .env
nano .env # Edit this

```
#### Python Operations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py compilemessages

```

#### Nginx & gunicorn Operations
- `sudo nano /etc/systemd/system/gunicorn.socket`
    ```raw
        [Unit]
        Description=gunicorn socket

        [Socket]
        ListenStream=/run/gunicorn.sock

        [Install]
        WantedBy=sockets.target
    ```
- `sudo nano /etc/systemd/system/gunicorn.service`
    ```raw
    [Unit]
    Description=gunicorn daemon
    Requires=gunicorn.socket
    After=network.target

    [Service]
    User=ubuntu
    Group=www-data
    WorkingDirectory=/home/ubuntu/agency
    ExecStart=/home/ubuntu/agency/venv/bin/gunicorn \
            --access-logfile - \
            --workers 3 \
            --bind unix:/run/gunicorn.sock \
            src.wsgi:application

    [Install]
    WantedBy=multi-user.target

    ```
```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket
file /run/gunicorn.sock
# Output : /run/gunicorn.sock: socket
# Check gunicorn socket's logs
sudo journalctl -u gunicorn.socket
sudo systemctl status gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```
- `sudo nano /etc/nginx/sites-available/agency`
    ```raw
    server {
        listen 80;
        server_name DOMAIN_or_IP_ADDRESS;

        location = /favicon.ico { access_log off; log_not_found off; }
        location /staticroot/ {
            root /home/ubuntu/agency;
        }

        location / {
            include proxy_params;
            proxy_pass http://unix:/run/gunicorn.sock;
        }
        
        location /media/ {
        root /home/ubuntu/agency;
        }
    }

    ```
- `sudo ln -s /etc/nginx/sites-available/agency /etc/nginx/sites-enabled`
- Remove default nginx file
```bash
sudo rm /etc/nginx/sites-enabled/default
```
- Test nginx
```bash
# Test your Nginx configuration for syntax errors:
sudo nginx -t
sudo systemctl restart nginx
```

##### In the end
```bash
sudo systemctl daemon-reload && sudo systemctl restart gunicorn.socket gunicorn.service nginx
```

#### Database Operations
```bash
sudo -u postgres psql
```
```psql
postgres=# CREATE DATABASE db_blog;
postgres=# CREATE USER userblog WITH PASSWORD 'passwordblog';
postgres=# ALTER ROLE userblog SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE userblog SET timezone TO 'UTC';
postgres=# GRANT ALL PRIVILEGES ON DATABASE myproject TO userblog;

```


#### Sources
- https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04

#### Security
- http://nginx.org/en/docs/http/ngx_http_limit_req_module.html
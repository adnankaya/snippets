# Database
```bash
# connecting to the database
$ psql -h hosting-address-of-blog.eu-central-1.rds.amazonaws.com --port=5432 -U adnankaya -d db_blog

# restore the database file to the specified db
$ psql -h hosting-address-of-blog.eu-central-1.rds.amazonaws.com --port=5432 -U adnankaya -d db_blog < agency_DUMP.sql

```
- postgres psyopg2 `sudo apt-get install libpq-dev`

# EC2 Ubuntu Server Installations
```bash

$ ls -l
-rw-rw-r-- 1 adnan adnan       1704 Nov 27 12:46 project-django.pem
$ chmod 400 project-django.pem
# connect to instance 
$ ssh -i project-django.pem ubuntu@aws.ip.address
# or
$ ssh -i project-django.pem ubuntu@aws.ip.address
# 1. install python3.8
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.8
$ sudo apt-get install python3.8-dev
# 2. install virtualenv
$ sudo apt-get install virtualenv
# 3. clone the project 
$ gh repo clone adnankaya/agency
# 4. inside the project create a new virtual environment
$ cd agency
$ virtualenv -p python3.8 venv
# 5. Activate the virtual environment
$ source venv/bin/activate
# 6. install the project requirements
(venv)$ pip install -r prod-requirements.txt
# ^^^^ (venv) points that you activated the virtual environment
# 7. install apache web server
$ sudo apt-get install apache2
# 8. install the mod_wsgi
$ pip install mod_wsgi
# 9. run mod_wsgi-express command
$ mod_wsgi-express module-config
# output will be like this
LoadModule wsgi_module "/home/ubuntu/agency/venv/lib/python3.8/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so"
WSGIPythonHome "/home/ubuntu/agency/venv"
# 10. Grab above(9. insruction) output, this is what you need to tell Apache where to find your new mod_wsgi version. Update wsgi.load file
$ sudo nano /etc/apache2/mods-available/wsgi.load
######## inside nano #####################
#LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so
LoadModule wsgi_module "/home/ubuntu/agency/venv/lib/python3.8/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so"
WSGIPythonHome "/home/ubuntu/agency/venv"
######### save and exit from nano ########
# 11. Ensure mod_wsgi is enabled
$ sudo a2enmod wsgi
# 12. Restart your apache service
$ sudo systemctl reload apache2
# 13. go to apache2 sites folder
$ cd /etc/apache2/sites-available/
# 14. create a new conf file for agency
$ sudo cp 000-default.conf agency.conf
# 15. open and edit agency.conf
$ sudo nano agency.conf
############### inside nano ###############################
<VirtualHost *:80>
#	ServerName localhost
#	ServerAdmin webmaster@localhost

	Alias /static /home/ubuntu/agency/staticroot
	<Directory /home/ubuntu/agency/staticroot>
		Require all granted
	</Directory>
# We use AWS S3 buckets
	#Alias /media /home/ubuntu/agency/media
	#<Directory /home/ubuntu/agency/media>
	#	Require all granted
	#</Directory>

	<Directory /home/ubuntu/agency/src>
        <Files wsgi.py>
            Require all granted
        </Files>
	</Directory>

	WSGIDaemonProcess www.agency.org python-home=/home/ubuntu/agency/venv python-path=/home/ubuntu/agency
	WSGIProcessGroup www.agency.org
	WSGIScriptAlias / /home/ubuntu/agency/src/wsgi.py


	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
############### save and exit from nano ###################
# 16. static files command for django
(venv) ubuntu@adnankaya:~/agency$ python manage.py collectstatic
# collectstatic command copies all static files to staticroot folder which is STATIC_ROOT in the settings.

# 17. Create .env file by copying .env.example.md AND edit with your credentials
$ cp .env.example.md .env

# [ LAST ] disable default apache conf and enable agency.conf and reload the apache
$ sudo a2dissite 000-default.conf 
$ sudo a2ensite agency.conf 
$ sudo systemctl reload apache2
```
## HTTPS configuration Example
```bash
<VirtualHost *:443>
        ServerAdmin webmaster@localhost
        # DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
        SSLEngine on
        SSLCertificateFile /etc/apache2/certificate/apache-certificate.crt
        SSLCertificateKeyFile /etc/apache2/certificate/apache.key
</VirtualHost>
```
- In `settings/production.py` use these configuration when you have SSL & HTTPS
```python
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
```

# S3 Bucket Information
- User AWS API KEY and SECRET KEY to connect to S3 Bucket in `.env` file.
```bash
export AWS_STORAGE_BUCKET_NAME="project-blog-django-website"
export AWS_S3_SIGNATURE_VERSION="s3v4"
export AWS_S3_REGION_NAME="eu-central-1"
```
# Github
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

# WSGI Apache
- mod_wsgi https://stackoverflow.com/a/61845216/5491260
- see logs
```bash
$ cat /var/log/apache2/access.log 
$ cat /var/log/apache2/error.log 

```
# ElasticSearch
- Edit `.env` file to enter credentials and run the following command
- `python manage.py update_index`


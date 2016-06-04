
apt-get install libapache2-mod-wsgi python-dev
a2enmod wsgi
pip install virtualenv 
cd
virtualenv venv
source venv/bin/activate
pip install Flask
cat <<EOT >> /etc/apache2/sites-available/vigilant-web-gallery.conf
<VirtualHost *:80>
		ServerName hermes.stuycs.org
		ServerAdmin root@hermes.stuycs.org
		WSGIScriptAlias / /var/www/vigilant-web-gallery/vigilant-web-gallery.wsgi
		<Directory /var/www/vigilant-web-gallery/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/vigilant-web-gallery/static
		<Directory /var/www/vigilant-web-gallery/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOT
a2ensite vigilant-web-gallery
cd /var/www/vigilant-web-gallery
cat <<EOT >> vigilant-web-gallery.wsgi
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/vigilant-web-gallery/")

from app import app as application
application.secret_key = "4U90jO1]70>L"
EOT 


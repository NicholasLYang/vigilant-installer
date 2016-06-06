#echo "Installing apache, mod-wsgi, python-dev"
apt-get install libapache2-mod-wsgi python-dev apache2 
a2enmod wsgi
pip install virtualenv 
cd /var/www/vigilant-web-gallery/vigilant-web-gallery
#echo "Creating virtualenv"
virtualenv vigilantenv 
source vigilantenv/bin/activate
#echo "Installing Flask"
pip install Flask 
read ip
touch /etc/apache2/sites-available/vigilant-web-gallery.conf
cat >  /etc/apache2/sites-available/vigilant-web-gallery.conf <<EOF
<VirtualHost *:80>
		ServerName $ip
		ServerAdmin nick@nicholasyang.com
		WSGIScriptAlias / /var/www/vigilantwebgallery/vigilantwebgallery.wsgi
		<Directory /var/www/vigilantwebgallery/vigilantwebgallery/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/vigilantwebgallery/vigilantwebgallery/static
		<Directory /var/www/vigilantwebgallery/vigilantwebgallery/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF
a2ensite vigilantwebgallery
cd /var/www/vigilantwebgallery
touch vigilantwebgallery.wsgi
cat >  vigilantwebgallery.wsgi <<EOF
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/vigilantwebgallery/")
activate_this = '/var/www/vigilantwebgallery/vigilantwebgallery/vigilantenv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from vigilantwebgallery import app as application
application.secret_key = "4U90jO1]70>L"
EOF
service apache2 restart
service apache2 reload




#echo "Installing apache, mod-wsgi, python-dev"
apt-get install libapache2-mod-wsgi python-dev apache2 
a2enmod wsgi
pip install virtualenv 
cd /var/www/WALK/WALK
#echo "Creating virtualenv"
virtualenv walkenv 
source walkenv/bin/activate
#echo "Installing Flask"
pip install Flask pymongo simplejson 

touch /etc/apache2/sites-available/vigilantwebgallery.conf
cat >  /etc/apache2/sites-available/vigilantwebgallery.conf <<EOF
<VirtualHost *:80>
		ServerName 162.243.68.25
		ServerAdmin nick@nicholasyang.com
		WSGIScriptAlias / /var/www/WALK/WALK.wsgi
		<Directory /var/www/WALK/WALK/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/WALK/WALK/static
		<Directory /var/www/WALK/WALK/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF
a2ensite WALK
cd /var/www/WALK
touch WALK.wsgi
cat >  WALK.wsgi <<EOF
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/WALK/")
activate_this = '/var/www/WALK/WALK/walkenv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from WALK import app as application
application.secret_key = "4U90jO1]70>L"
EOF
service apache2 restart
service apache2 reload




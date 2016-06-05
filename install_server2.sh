echo "Installing apache, mod-wsgi, python-dev"
apt-get install libapache2-mod-wsgi python-dev apache2 &> /dev/null 
a2enmod wsgi
pip install virtualenv &> /dev/null 
cd /var/www/vigilant-web-gallery/vigilant-web-gallery
echo "Creating virtualenv"
virtualenv vigilantenv &> /dev/null 
source vigilantenv/bin/activate
echo "Installing Flask"
pip install Flask &> /dev/null 
echo "Adding config"
echo "What is the ip?"
read ip
touch /etc/apache2/sites-available/vigilant-web-gallery.conf
cat >  /etc/apache2/sites-available/vigilant-web-gallery.conf <<EOF
<VirtualHost *:80>
		ServerName $ip
		ServerAdmin root@162.243.105.166
		WSGIScriptAlias / /var/www/vigilant-web-gallery/vigilant-web-gallery.wsgi
		<Directory /var/www/vigilant-web-gallery/vigilant-web-gallery/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/vigilant-web-gallery/vigilant-web-gallery/static
		<Directory /var/www/vigilant-web-gallery/vigilant-web-gallery/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF
a2ensite vigilant-web-gallery
cd /var/www/vigilant-web-gallery
touch vigilant-web-gallery.wsgi
cat >  vigilant-web-gallery.wsgi <<EOF
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/vigilant-web-gallery/")

from vigilant-web-gallery import app as application
application.secret_key = "4U90jO1]70>L"
EOF
service apache2 restart
service apache2 reload




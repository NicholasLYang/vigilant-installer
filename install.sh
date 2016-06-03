mkdir /usr/www
sudo apt-get update
sudo apt-get install Imagemagick python-pip sqlite emacs git
echo "What is your domain? I.e. www.YOUR_DOMAIN_HERE.com"
read domain
git clone https://github.com/daisyb/vigilant-web-gallery.git /usr/www/www.$domain.com

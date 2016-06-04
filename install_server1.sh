#!/bin/sh
# assumes sshed into server with ROOT access
mkdir /var/www
apt-get update
apt-get install Imagemagick python-pip sqlite emacs git
mkdir /var/www/vigilant-web-gallery/
cd /var/www/vigilant-web-gallery
git clone https://github.com/daisyb/vigilant-web-gallery.git 
cd /var
mkdir repo && cd repo
mkdir site.git && cd site.git
git init --bare
cd hooks
touch post-receive
printf  "#!/bin/sh" > post-receive
printf  "git --work-tree=/var/www/vigilant-web-gallery --git-dir=/var/repo/site.git checkout -f" > post-receive
chmod +x post-receive



#!/bin/sh
# assumes sshed into server with ROOT access
mkdir /var/www
apt-get update
apt-get install Imagemagick python-pip sqlite emacs git
echo "What is your domain? "
read domain
git clone https://github.com/daisyb/vigilant-web-gallery.git /usr/www/$domain
echo "Are you the master of your domain?"
cd /var
mkdir repo && cd repo
mkdir site.git && cd site.git
git init --bare
cd hooks
touch post-receive
echo "#!/bin/sh" post-receive
echo "git --work-tree=/var/www/domain.com --git-dir=/var/repo/site.git checkout -f" post-receive
chmod +x post-receive



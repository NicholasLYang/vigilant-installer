#!/bin/sh
# assumes sshed into server with ROOT access
mkdir /var/www
echo "Installing imagemagick, pythonmagick, pip, sqlite, git, emacs"
apt-get update 
apt-get install Imagemagick python-pythonmagick python-pip sqlite emacs git 
echo "Making directories..."
mkdir /var/www/vigilant-web-gallery/
mkdir /var/www/vigilant-web-gallery/vigilant-web-gallery
echo "Setting up remote"
cd /var
mkdir repo && cd repo
mkdir site.git && cd site.git
git init --bare 
cd hooks
touch post-receive
printf  "#!/bin/sh" > post-receive
printf  "git --work-tree=/var/www/vigilant-web-gallery/vigilant-web-gallery --git-dir=/var/repo/site.git checkout -f" > post-receive
chmod +x post-receive



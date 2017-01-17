#!/bin/sh
# assumes sshed into server with ROOT access
mkdir /var/www
apt-get update
apt-get install imagemagick python-pythonmagick python-pip sqlite emacs git
apt install python-pip
#echo "Making directories..."
mkdir /var/www/vigilantwebgallery/
mkdir /var/www/vigilantwebgallery/vigilantwebgallery
#secho "Setting up remote"
cd /var
mkdir repo && cd repo
mkdir site.git && cd site.git
git init --bare 
cd hooks
touch post-receive
printf  "#!/bin/sh" > post-receive
printf  "git --work-tree=/var/www/vigilantwebgallery/vigilantwebgallery --git-dir=/var/repo/site.git checkout -f" > post-receive
chmod +x post-receive



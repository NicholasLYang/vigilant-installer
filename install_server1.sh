#!/bin/sh
# assumes sshed into server with ROOT access
mkdir /var/www
apt-get update 
apt-get install monogdb python-pythonmagick python-pip emacs git 
#echo "Making directories..."
mkdir /var/www/WALK/
mkdir /var/www/WALK/WALK
#secho "Setting up remote"
cd /var
mkdir repo && cd repo
mkdir site.git && cd site.git
git init --bare 
cd hooks
touch post-receive
printf  "#!/bin/sh" > post-receive
printf  "git --work-tree=/var/www/WALK/WALK --git-dir=/var/repo/site.git checkout -f" > post-receive
chmod +x post-receive



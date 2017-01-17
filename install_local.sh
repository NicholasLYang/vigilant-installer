#!/bin/sh

ssh root "apt-get install git; git clone https://github.com/NicholasLYang/vigilant-installer.git; cd vigilant-installer; . install_server1.sh"
cd ..
# git clone git@github.com:daisyb/vigilant-web-gallery.git &> /dev/null 
cd vigilant-web-gallery
git remote rm vigilant-live
git remote add vigilant-live ssh://root/var/repo/site.git
touch README
git add README
git commit -m 'testing remote'
git push vigilant-live master
ssh root "cd vigilant-installer; . install_server2.sh"




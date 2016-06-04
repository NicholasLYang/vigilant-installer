#!/bin/sh

ssh grimes "apt-get install git; git clone https://github.com/NicholasLYang/vigilant-installer.git; cd vigilant-installer; . install_server1.sh"
cd ..
git clone git@github.com:daisyb/vigilant-web-gallery.git
cd vigilant-web-gallery
git remote add vigilant-live ssh://root@hermes.stuycs.org/var/repo/site.git
ssh grimes "cd vigilant-installer; . install_server2.sh"




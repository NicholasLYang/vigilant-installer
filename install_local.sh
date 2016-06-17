#!/bin/sh
cat > ~/.ssh/config <<EOF
Host grimes
    HostName 162.243.68.25
    User root
EOF
ssh grimes "apt-get install git; git clone https://github.com/NicholasLYang/vigilant-installer.git; cd vigilant-installer; . install_server1.sh"
cd ..
 git clone https://github.com/wayez/WALK.git
cd WALk
git remote rm WALK-live
git remote add WALK-live ssh://grimes/var/repo/site.git
touch README
git add README
git commit -m 'testing remote'
git push WALK-live master
ssh grimes "cd vigilant-installer; . install_server2.sh"




#!/bin/sh
echo "Please give server IP"
read ip



ssh root@$ip "apt-get install git; git clone https://github.com/NicholasLYang/vigilant-installer.git; cd vigilant-installer; . install_server_1.sh"




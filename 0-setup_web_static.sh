#!/usr/bin/env bash
# set up dummy html

server="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
root="\troot /data/web_static/releases/test/index.html;\n"
old="root /usr/share/nginx/html;"
file="/etc/nginx/sites-available/default"
apt-get update -y
apt-get install nginx -y
mkdir -p "/data/web_static/releases/test/"
echo -e "Holberton" > "/data/web_static/releases/test/index.html"
rm -f "/data/web_static/current"; ln -s "/data/web_static/releases/test/" "/data/web_static/current"
# chown -h ubuntu:ubuntu "/data/"
sed -i 's/"$old"/"$root"/' "$file"
sed -i "29i\ $server" "$file"
service nginx restart

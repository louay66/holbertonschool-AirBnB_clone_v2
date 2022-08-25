#!/usr/bin/env bash
# setup web servers for the deployment of web_static

config="
server {
	listen 80 default_server;
	server_name _;
	location / {
		try_files \$uri \$uri/ =404;
	}
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html;
		try_files \$uri \$uri /hbnb_static/index.html;
	}
}
"
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "<h1>in here just test</h1>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
echo -e "$config" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart

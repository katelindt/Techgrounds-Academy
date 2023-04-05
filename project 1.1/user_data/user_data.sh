#!/bin/bash

sudo yum update -y
sudo yum install -y httpd 
sudo systemctl start httpd
sudo systemctl enable httpd

sudo su -c "echo lalala > /var/www/html/index.html"
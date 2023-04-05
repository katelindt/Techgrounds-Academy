#!/bin/bash

sudo yum update -y
sudo yum install -y httpd 
sudo systemctl start httpd
sudo systemctl enable httpd

echo "<h1> Hello world, this is the website to test if it's working</h1>" | sudo tee index.html
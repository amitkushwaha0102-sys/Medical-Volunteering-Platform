#!/bin/bash

echo "system updating"
sudo apt update
echo "System updated"



sudo apt install -y docker.io

sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu


cd /home/ubuntu
git clone https://github.com/amitkushwaha0102-sys/Medical-Volunteering-Platform.git
cd Medical-Volunteering-Platform


docker build -t medical-volunteering ./backend


docker run -d \
  --name medical-app \
  -p 5000:5000 \
  -e DATABASE_URL=$DATABASE_URL \
  -e SECRET_KEY=$SECRET_KEY \
  medical-volunteering
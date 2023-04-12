# To get docker-compose on EC2 instance
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose version

# To build and run db container
docker-compose up -d

# To run web service using gunicorn
gunicorn --bind 0.0.0.0:55555 my_resume.wsgi

# Or create service
sudo nano /etc/systemd/system/gunicorn.service

# Edit /etc/services adding the port 8000 to the list

# Install and make sure it is running firewalld
sudo firewall-cmd --zone=public --add-port=8000/tcp --permanent

# To troubleshoot further: https://repost.aws/knowledge-center/ec2-instance-hosting-unresponsive-website


## NGINX Server Configuration

#### 1. Install NGINX On the Server
This step depends on the Linux distribution.  For Ubuntu, this is:
```
sudo apt install nginx
```

#### 2. Replace the nginx.conf file with the one in this directory
For example:
```
sudo cp awsops/nginx/nginx.conf /etc/nginx/nginx.conf
```

#### 3. Install and run certbot
There are useful instructions here: https://certbot.eff.org

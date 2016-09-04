## Vagrant dev setup on Windows (VirtualBox, Vagrant, Git required)
1. git clone https://bitbucket.org/want-will-wont/want-will-wont.git
2. in project root: vagrant up
3. ssh to 127.0.0.1:2222 (user/password: vagrant/vagrant)
4. sudo apt-get install python3-pip libpq-dev
5. cd /vagrant
6. pip3 install -r requirements.txt
7. python3 manage.py runserver 0.0.0.0:8000

## Live setup on Ubuntu 16.04
## Follow common Linux sense and pick your installation directory, create a new user, database user, etc. Google it if necessary
1. git clone https://bitbucket.org/want-will-wont/want-will-wont.git
2. sudo apt-get install python3-pip libpq-dev supervisor nginx postgresql postgresql-contrib
3. virtualenv -p /usr/bin/python3.5 venv
4. source venv/bin/activate
5. cd want-will-wont
6. pip install -r requirements.txt
7. copy sexquizit.nginx, paste to /etc/nginx/sites-enabled/sexquizit and make sure upstream and static folder are set correctly
8. /etc/init.d/nginx restart
9. copy sexquizit.supervisor, paste to /etc/supervisor/conf.d/sexquizit.conf, check that command and environment are correct
10. see that your local.py settings file points to the correct database, be sure DEBUG=False and ALLOWED_HOSTS=['.sexquiz.it'] are in there
11. python manage.py collectstatic
12. python manage.py compress --force
13. check that your production-uwsgi.sh has correct paths set
14. service supervisor restart
## Dev setup with Vagrant
1) git clone https://bitbucket.org/want-will-wont/want-will-wont.git
2) in project root: vagrant up
3) ssh to 127.0.0.1:2222 (user/password: vagrant/vagrant)
4) cd /vagrant
5) sudo apt-get install python3-pip
6) pip3 install -r requirements.txt
7) Python-Postgres driver may need: sudo apt-get install libpq-dev
8) python3 manage.py runserver 0.0.0.0:8000
9) visit localhost:8000



#!/bin/bash
export HOME=/home/sexquizit
cd $HOME
source sexquizit/bin/activate
cd $HOME/want-will-wont/
uwsgi --socket /home/sexquizit/want-will-wont/sexquizit.sock --module want_will_wont.wsgi --chmod-socket=777 --env=LANG="en_US.utf8"
exit $?
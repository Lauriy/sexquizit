#!/bin/bash
export HOME=/home/sexquizit
cd $HOME
source venv/bin/activate
cd $HOME/want-will-wont/
uwsgi --socket /home/sexquizit/want-will-wont/sexquizit.sock --processes=1 --module want_will_wont.wsgi --chmod-socket=777 --env=LANG="en_US.utf8"
exit $?
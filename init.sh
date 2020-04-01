sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s home/box/etc/hello.py /etc/gunicorn.d/hello.py
sudo gunicorn -c /home/box/web/etc/hello.py hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/ask.conf.py ask.wsgi:application

import os, uuid
import time

from django.core.management.base import BaseCommand

from ugh import settings

class Command(BaseCommand):
    help = 'Run production server'

    def add_arguments(self, parser):
        parser.add_argument(
            '--serve-static',
            help='Serve static files as well',
            action='store_true'
        )

    def handle(self, *args, **options):
        if settings.DEBUG is True:
            i = input('DEBUG is on. Are you sure you want to run in production mode? [y/N]')
            if i.strip().lower().startswith('y') is False:
                return
        daphne_port = '8000'
        when_interrupted = lambda: print('interrupted')
        if options['serve_static']:
            daphne_port = '9000'
            print('serving static files')
            has_nginx = os.system('hash nginx >/dev/null 2>&1') == 0
            if has_nginx is False:
                print("You need to install nginx in order to serve static files!")
                return
            print('nginx is listening at 127.0.0.1:8000')
            os.system(f'nginx -c {self.gen_nginx_conf()}')
            when_interrupted = lambda: os.system(f'kill {str(self.get_nginx_pid())}')
        os.system(f'/usr/bin/env python -m daphne -p {daphne_port} ugh.asgi:application')
        when_interrupted()

    def gen_nginx_conf(self, daphne_port=9000):
        nginx_pid = os.path.join(settings.EXTERNAL_FILES_DIR, 'nginx/nginx.pid')
        nginx_access_log = os.path.join(settings.EXTERNAL_FILES_DIR, 'nginx/access.log')
        nginx_error_log = os.path.join(settings.EXTERNAL_FILES_DIR, 'nginx/error.log')

        with open(os.path.join(settings.EXTERNAL_FILES_DIR, 'nginx/nginx_conf.template')) as c:
            nginx_template = c.read()
        nginx_template = nginx_template.replace('____NGINX_PID____', nginx_pid)
        nginx_template = nginx_template.replace('____NGINX_ACCESS_LOG____', nginx_access_log)
        nginx_template = nginx_template.replace('____NGINX_ERROR_LOG____', nginx_error_log)
        nginx_template = nginx_template.replace('____STATIC_URL____', settings.STATIC_URL.rstrip('/'))
        nginx_template = nginx_template.replace('____STATIC_ROOT____', settings.STATIC_ROOT)
        nginx_template = nginx_template.replace('____DAPHNE_PORT____', str(daphne_port))
        conf = os.path.join(settings.EXTERNAL_FILES_DIR, 'nginx/nginx.conf')
        with open(conf, 'w') as c:
            c.write(nginx_template)
        return conf
    def get_nginx_pid(self):
        try:
            with open(os.path.join(settings.EXTERNAL_FILES_DIR, 'nginx/nginx.pid')) as p:
                pid = int(p.read())
        except FileNotFoundError:
            pid = 0
        return pid

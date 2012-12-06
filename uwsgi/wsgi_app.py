#! /usr/bin python

import sys
import os
import django.core.handlers.wsgi

sys.path.append('/var/www/python')
os.environ['DJANGO_SETTINGS_MODULE'] = 'slx.settings'
application = django.core.handlers.wsgi.WSGIHandler()


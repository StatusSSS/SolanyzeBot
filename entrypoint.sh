#!/bin/sh

exec gunicorn -c /opt/app-root/src/api/config/gunicorn_conf.py api.application:fast_api
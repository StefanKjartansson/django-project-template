#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
"""
"""
from gevent import monkey
from socketio.server import SocketIOServer

monkey.patch_all()

from {{ project_name }}.wsgi import application
from {{ project_name }} import settings

from django.core.management.commands.runserver import DEFAULT_PORT


if settings.DEBUG:
    from django.contrib.staticfiles.handlers import StaticFilesHandler
    application = StaticFilesHandler(application)


if __name__ == '__main__':
    print('Listening on http://127.0.0.1:%s and on port 10843 (flash policy server)' % DEFAULT_PORT)
    SocketIOServer(('0.0.0.0', int(DEFAULT_PORT)),
        application,
        resource="socket.io",
        policy_server=True).serve_forever()

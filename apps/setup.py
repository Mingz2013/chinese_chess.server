# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import sys

from twisted.python import log
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor
from autobahn.twisted.resource import WebSocketResource, WSGIRootResource

if __name__ == "__main__":

    try:
        from imp import reload

        reload(sys)
        sys.setdefaultencoding('utf8')
    except (AttributeError, NameError):
        print "set default coding utf-8 error"
        pass

    log.startLogging(sys.stdout)

    from ws.chat_app import create_chat_ws_resource
    from ws.game_app import create_game_ws_resource
    from flask_app import create_app

    flask_app = create_app('default')
    chat_ws_resource = create_chat_ws_resource()
    game_ws_resource = create_game_ws_resource()

    # create a Twisted Web WSGI resource for our Flask server
    wsgiResource = WSGIResource(reactor, reactor.getThreadPool(), flask_app)

    # create a root resource serving everything via WSGI/Flask, but
    # the path "/ws" served by our WebSocket stuff
    rootResource = WSGIRootResource(
        wsgiResource,
        {
            'ws_chat': chat_ws_resource,
            'ws_game': game_ws_resource
        }
    )

    # create a Twisted Web Site and run everything
    site = Site(rootResource)

    reactor.listenTCP(8080, site)
    reactor.run()

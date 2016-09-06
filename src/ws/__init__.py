# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol

from autobahn.twisted.resource import WebSocketResource, WSGIRootResource


# Our WebSocket Server protocol
class WSServerProtocol(WebSocketServerProtocol):

    def onMessage(self, payload, isBinary):
        print isBinary
        print payload
        if isBinary:
            pass
        else:
            pass
        self.sendMessage(payload, isBinary)


def create_ws_resource():
    # create a Twisted Web resource for our WebSocket server
    wsFactory = WebSocketServerFactory(u"ws://127.0.0.1:8080")
    wsFactory.protocol = WSServerProtocol
    wsResource = WebSocketResource(wsFactory)
    return wsResource

# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol

from autobahn.twisted.resource import WebSocketResource, WSGIRootResource


# Our WebSocket Server protocol
class EchoServerProtocol(WebSocketServerProtocol):
    def onMessage(self, payload, isBinary):
        self.sendMessage(payload, isBinary)


def create_ws_resource():
    # create a Twisted Web resource for our WebSocket server
    wsFactory = WebSocketServerFactory(u"ws://127.0.0.1:8080")
    wsFactory.protocol = EchoServerProtocol
    wsResource = WebSocketResource(wsFactory)
    return wsResource

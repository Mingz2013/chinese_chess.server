# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from autobahn.twisted.websocket import WebSocketServerProtocol


# Our WebSocket Server protocol
class ChatWSServerProtocol(WebSocketServerProtocol):
    def onConnect(self, request):
        print("Client connecting: {}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {} bytes".format(len(payload)))
        else:
            print("Text message received: {}".format(payload.decode('utf8')))

            # obj = json.loads(payload.decode('utf8'))
            # payload = json.dumps(obj, ensure_ascii=False).encode('utf8')

        ## echo back message verbatim
        self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {}".format(reason))

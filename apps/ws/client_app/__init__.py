# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import sys

from twisted.internet import reactor
from twisted.python import log

from autobahn.twisted.websocket import WebSocketClientFactory, \
    WebSocketClientProtocol, \
    connectWS


class PingClientProtocol(WebSocketClientProtocol):
    def onOpen(self):
        self.pingsReceived = 0
        self.pongsSent = 0

    def onClose(self, wasClean, code, reason):
        reactor.stop()

    def onPing(self, payload):
        self.pingsReceived += 1
        print("Ping received from {} - {}".format(self.peer, self.pingsReceived))
        self.sendPong(payload)
        self.pongsSent += 1
        print("Pong sent to {} - {}".format(self.peer, self.pongsSent))


if __name__ == '__main__':

    log.startLogging(sys.stdout)

    if len(sys.argv) < 2:
        print("Need the WebSocket server address, i.e. ws://127.0.0.1:9000")
        sys.exit(1)

    factory = WebSocketClientFactory(sys.argv[1])
    factory.protocol = PingClientProtocol
    connectWS(factory)

    reactor.run()

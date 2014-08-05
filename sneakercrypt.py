import sys # required for logging
from classes import *
from modules import *
from twisted.python import log
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerFactory

if __name__ == '__main__':

	log.startLogging(sys.stdout)
	while True:
		
		messageToSend = input("Enter a message to send")

		factory = WebSocketServerFactory()
		factory.protocol = serverProtocol

		reactor.listenTCP(9000, factory)
		reactor.run()

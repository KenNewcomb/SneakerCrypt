import sys # required for logging
from classes import *
from modules import *
from twisted.python import log
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerFactory

if __name__ == '__main__':

	log.startLogging(sys.stdout) # Start logging to console
	mode = sys.argv[0] # Get server mode from cmdline argument.

	if mode == "server": # Start server
		factory = WebSocketServerFactory()
		factory.protocol = serverProtocol
		reactor.listenTCP(9000, factory)
		reactor.run()
	elif mode == "client": # Start client
		factory = WebSocketClientFactory()
		factory.protocol = MyClientProtocol
		reactor.connectTCP("127.0.0.1", 9000, factory)
		reactor.run()
	
	messageToSend = input("Enter a message to send:")


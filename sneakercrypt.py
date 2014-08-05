import sys # required for logging
from classes.serverprotocol import serverProtocol
from classes.clientprotocol import clientProtocol
from modules import *
from twisted.python import log
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerFactory
from autobahn.twisted.websocket import WebSocketClientFactory

if __name__ == '__main__':

	log.startLogging(sys.stdout) # Start logging to console
	mode = sys.argv[1] # Get server mode from cmdline argument.
	if mode == "server": # Start server
		factory = WebSocketServerFactory()
		factory.protocol = serverProtocol
		reactor.listenTCP(9000, factory)
		reactor.run()
	elif mode == "client": # Start client
		factory = WebSocketClientFactory()
		factory.protocol = clientProtocol
		reactor.connectTCP("127.0.0.1", 9000, factory)
		reactor.run()
	else:
		print("Error. Please see documentation for usage instructions.")
		sys.exit(0)

	while(True):
		messageToSend = input("Enter a message to send:")

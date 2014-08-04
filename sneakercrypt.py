import sys # required for logging
from classes import *
from modules import *
######################################################################
# Current demonstration of functionality (uncomment desired section) #
######################################################################

if __name__ == '__main__':

	from classes.serverprotocol import serverProtocol
	from twisted.python import log
	from twisted.internet import reactor
	log.startLogging(sys.stdout)

	from autobahn.twisted.websocket import WebSocketServerFactory
	factory = WebSocketServerFactory()
	factory.protocol = serverProtocol

	reactor.listenTCP(9000, factory)
	reactor.run()

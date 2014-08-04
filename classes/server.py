if __name__ == '__main__':
	
	import sys
	
	from twisted.python import log
	from twisted.python import reactor
	log.startLogging(sys.stdout)

	from autobahn.twisted.websocket import WebSocketServerFactory

	factory = WebSocketServerFactory()
	factory.protocol = MyServerProtocol

	reactor.listenTCP(9000, factory)
	reactor.run

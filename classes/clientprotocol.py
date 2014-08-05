from autobahn.twisted.websocket import WebSocketClientProtocol

class MyClientProtocol(WebSocketClientProtocol):

	def onConnect(self):
		## Do something...

	def onOpen(self):
		self.sendMessage(u"Hello, world!".encode('utf8'))

	def onMessage(self, payload, isBinary):
		if isBinary:
			print("Binary message received: {0} bytes".format(len(payload)))
		else:
			print("Text message received: {0}".format(payload.decode('utf8')))

	def onClose(self):
		## Do something...

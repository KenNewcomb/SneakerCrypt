from autobahn.twisted.websocket import WebSocketServerProtocol

class serverProtocol(WebSocketServerProtocol):

	def onConnect(self, response):
		print("Connected to Server: {}".format(response.peer))
	
	def onOpen(self):
		print("WebSocket connection open")
`
	def onMessage(self, payload, isBinary):
		## echo back message
		self.sendMessage(payload, isBinary)
		s = payload.decode('utf8')
		payload = s.encode('utf8')
		self.sendMessage(payload, isBinary = False)

from autobahn.twisted.websocket import WebSocketClientProtocol
import time

class clientProtocol(WebSocketClientProtocol):

	def onConnect(self, response):
		print("hello")
	def onOpen(self):
		print("Client onOpen()")
	def onMessage(self, payload, isBinary):
		if isBinary:
			print("Binary message received: {0} bytes".format(len(payload)))
		else:
			print("Text message received: {0}".format(payload.decode('utf8')))

	def onClose(self, wasClean, code, reason):
		print("Connection closed.")

	def messageSender(self):
			message = input("Message:")
			self.sendMessage(message.encode('utf8'))

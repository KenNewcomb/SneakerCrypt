"""
This class defines a Message object. There are three steps required for Message encryption/decryption:
1. String to binary conversion
2. Message padding
3. Encryption with key

Each step of the encryption process has a function and boolean value associated with it.
"""
class Message:

	def __init__(self, message):
		self.message = message
		self.isBinary = False
		self.isPadded = False
		self.isEncrypted = False

	def toBinary(self):
		"Converts a string message to a binary string format"
		letter_array = [ord(c) for c in self.message]
		self.message =  "".join([bin(letter)[2:] for letter in letter_array])
	
	def pad(self):
		"Ensures that a binary message is 1600 bits long to obfuscate the true message length"
		while(len(self.message) < 1600):
			self.message += "0"
		self.isPadded = True

	def encrypt(self,key):
		"Encrypts the message with the given key"
		cryptobits = list(zip(key,self.message))
		cypher = []
		for pair in cryptobits:
			pair = ord(pair[0]) ^ ord(pair[1])
			cypher.append(pair)
		self.message =  "".join([str(bit) for bit in cypher])
		self.isEncrypted = True
	
	def decrypt(self,key):
		"Decrypts the message with given key"
		cryptobits = list(zip(key,self.message))
		message = []
		for pair in cryptobits:
			pair = ord(pair[0]) ^ ord(pair[1])
			message.append(pair)
		self.message = "".join([str(bit) for bit in message])
		self.isEncrypted = False

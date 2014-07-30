class Message:

	def __init__(self, message):
		self.message = message
		self.isEncrypted = False
		self.isPadded = False

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
		cryptobits = list(zip(bin(key)[2:],self.message))
		cypher = []
		for pair in cryptobits:
			pair = ord(pair[0]) ^ ord(pair[1])
			cypher.append(pair)
		print(cypher)
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

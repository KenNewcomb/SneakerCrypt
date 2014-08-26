"""
This class defines a Message object. There are three steps required for Message encryption/decryption:
1. String to binary conversion
2. Message padding
3. Encryption with key
"""
class Message:

	def __repr__(self):
		return self.message

	def __init__(self, message):
		self.message = message

	def toBinary(self):
		"Converts a string message to a binary string format"
		letter_array = [ord(c) for c in self.message]
		binary_array = []
		for letter in letter_array:
			letter = format(letter, "08b")
			binary_array.append(letter)
		self.message =  "".join([letter for letter in binary_array])
	
	def pad(self):
		"Ensures that a binary message is 1600 bits long to obfuscate the true message length"
		while(len(self.message) < 1600):
			self.message += "0"

	def encrypt(self,key):
		"Encrypts the message with the given key"
		cryptobits = list(zip(bin(key)[2:],self.message))
		cypher = []
		for pair in cryptobits:
			pair = ord(pair[0]) ^ ord(pair[1])
			cypher.append(pair)
		self.message =  "".join([str(bit) for bit in cypher])
	
	def decrypt(self,key):
		"Decrypts the message with given key"
		cryptobits = list(zip(bin(key)[2:],self.message))
		message = []
		for pair in cryptobits:
			pair = ord(pair[0]) ^ ord(pair[1])
			message.append(pair)
		self.message = "".join([str(bit) for bit in message])

	def depad(self):
		"Parses the binary stream, byte by byte, and removes the padding."
		plaintext = []
		i = 0
		while self.message[i:i+8] != '00000000': #end of data
			plaintext.append(self.message[i:i+8])
			i = i + 8
		self.message = "".join([str(letter) for letter in plaintext])

	def toString(self):
		"Converts a binary, utf-8 message into a readable string"
		i = 0
		plaintext = []
		while i < len(self.message):
			plaintext.append(chr(int((self.message[i:i+8]),2)))
			i = i + 8
		self.message = "".join([str(letter) for letter in plaintext])

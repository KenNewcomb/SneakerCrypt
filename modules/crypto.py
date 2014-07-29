# This file will handle cryptographic functions.

def messageToBinary(message):
	"Converts a string message to a binary string format"
	letter_array = [ord(c) for c in message]
	return "".join([bin(letter)[2:] for letter in letter_array])

def padMessage(binary_string):
	"Ensures that a binary message is 1600 bits long to obfuscate the true message length"
	while(len(binary_string) < 1600):
		binary_string += "0"
	return binary_string

def encrypt(key,binary_string):
	cryptobits = list(zip(key,binary_string))
	cypher = []
	for pair in cryptobits:
		pair = ord(pair[0]) ^ ord(pair[1])
		cypher.append(pair)
	return "".join([str(bit) for bit in cypher])

# This file will handle cryptographic functions.

def messageToBinary(message):
	"Converts a string message to a binary format"
	ascii =  int("".join(str(ord(c)) for c in message))
	binary_message = bin(ascii)[2:]
	return str(binary_message)

def padMessage(bin_message):
	"Ensures that a binary message is 200 characters long to obfuscate the true message length"
	while(len(bin_message) < 1600):
		bin_message += '0'
	return bin_message

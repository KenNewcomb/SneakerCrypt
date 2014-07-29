# This file will handle cryptographic functions.

def messageToBinary(message):
	"Converts a string message to a binary format"
	ascii =  int("".join(str(ord(c)) for c in message))
	binary_message = bin(ascii)[2:]
	return str(binary_message)

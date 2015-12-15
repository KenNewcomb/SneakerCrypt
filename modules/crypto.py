""" crypto.py: An implementation of one-time-pad cryptography."""
import sys

def getMessage():
	print("A Sneakercrypt message can be 200 characters long.")
	message = input("Message : ")
	return message

def encrypt(pad):
	"""Encrypts the message with the given pad."""
	# Get message.
	message = getMessage()
	
	# Convert message to byte array
	message_bytes = bytearray(message, 'utf-8')
	pad_bytes     = bytearray(pad, 'utf-8')
	
	cypherints = []
	for byte in range(0, len(message_bytes)):
		# xor returns an int, which is what a bytearray.append(int) expects
		cypherchar = message_bytes[byte] ^ pad_bytes[byte]
		cypherints.append(hex(cypherchar))
	for number in cypherints:
		sys.stdout.write(number)
	sys.stdout.write("\n")
	sys.stdout.flush()

def decrypt(pad):
	"""Decrypts given message with given pad."""
	message = getMessage()

	message_bytes = bytearray(message, 'hex')
	pad_bytes     = bytearray(pad, 'utf-8')
	
	for byte in range(0, len(message_bytes)):
		plainchar = message_bytes[byte] ^ pad_bytes[byte]
		plaintext.append(plainchar)

	for number in plaintext:
		sys.stdou.write(number)

	sys.stdout.write("\n")
	sys.stdout.flush()

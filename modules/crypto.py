""" crypto.py: An implementation of one-time-pad cryptography."""
import sys

def getMessage():
	message = input("Message : ")
	return message

def binaryMessage(message):
	"""Converts a message into a padded 200-character bytearray."""
	# Convert message to byte array
	message_bytes = bytearray(message, 'utf-8')
	
	# Make sure message is <= 200 characters
	if len(message_bytes) > 200:
		print("Message is longer than 200 characters. Sneakercrypt will abort.")
		exit()
	
	# Pad message to 200 characters:
	while len(message_bytes) < 200:
		message_bytes.append(0)
	
	return message_bytes

def encrypt(pad):
	"""Encrypts the message with the given pad."""
	# Get message
	print("A Sneakercrypt message can be 200 characters long.")
	message = getMessage()
	message_bytes = binaryMessage(message)
	
	# Construct a bytearray from the pad.
	pad_bytes = bytearray(pad)
	
	# XOR message with pad to encrypt.
	cypherbits = []
	for byte in range(0, len(message_bytes)):
		cypherchar = message_bytes[byte] ^ pad_bytes[byte]
		cypherbits.append(cypherchar)
	
	print("Encrypted Cyphertext:")
	for bit in cypherbits:
		sys.stdout.write(str(bit) + '$')
	sys.stdout.write("\n")
	sys.stdout.flush()
	

def decrypt(pad):
	"""Decrypts given message with given pad."""
	# Parse message and construct bytearray
	message = getMessage().split('$')[:-1]
	message_bytes = bytearray()
	for word in message:
		message_bytes.append(int(word))

	# Construct a bytearray from the pad.
	pad_bytes = bytearray(pad)

	# ...and again, XOR message with pad to decrypt.
	plaintext = bytearray()
	for byte in range(0, len(message_bytes)):
		plainchar = message_bytes[byte] ^ pad_bytes[byte]
		plaintext.append(plainchar)

	print("Decrypted Plaintext:")
	print(plaintext.decode('utf-8'))

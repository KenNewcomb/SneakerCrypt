""" crypto.py: An implementation of one-time-pad cryptography."""

def getMessage():
	print("A Sneakercrypt message can be 200 characters long.")
	message = input("Message : ")
	return message

def encrypt(name, pad):
	"""Encrypts the message with the given pad."""
	# Get message.
	message = getMessage()

	# Convert message to byte array
	message_bytes = bytearray(message, 'utf-8')
	pad_bytes     = bytearray(pad, 'utf-8')

	cyphertext = bytearray()
	for byte in message_bytes:
		cypherchar = byte ^ pad_bytes[message_bytes.index(byte)]
		cyphertext.append(cypherchar)
	print(cyphertext)
	print(type(cyphertext))
	print(cyphertext.decode('utf-8'))
	
	plaintext = bytearray()
	for byte in cyphertext:
		plainchar = byte ^ pad_bytes[cyphertext.index(byte)]
		plaintext.append(plainchar)
	print(plaintext)
	print(type(plaintext))
	print(plaintext.decode('utf-8'))

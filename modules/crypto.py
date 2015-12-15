""" crypto.py: An implementation of one-time-pad cryptography."""

def getMessage():
	print("A Sneakercrypt message can be 200 characters long.")
	message = input("Message :")
	return message

def encrypt(name, pad):
	"""Encrypts the message with the given pad."""
	# Get message.
	message = getMessage()

	# Convert message to byte array


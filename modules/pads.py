""" pads.py: Reads/manipulates pads from ./pads """
import os

def readPads():
	"""Read the list of pads from the disk."""
	inpads  = os.listdir('./inpads')
	outpads = os.listdir('./outpads')
	return [inpads, outpads]

def getUser(usernumber, padtype):
	"""Get the username, given the usernumber."""
	if padtype == 'inpad':
		# readPads()[0] = inpads
		user = readPads()[0][usernumber]
	else:
		# readPads()[1] = outpads
		user = readPads()[1][usernumber]

	return user

def getPad(user, padtype):
	"""Read a user's pad."""
	# If the user gives an pad ID
	try:
		usernumber = int(user) - 1
		user = getUser(usernumber, padtype)
	except ValueError:
		# the user gave a username, no problem
		pass
	
	# If the user gives a username
	try:
		pad = open('./{0}s/{1}'.format(padtype, user), 'rb').read()
		return pad
	except FileNotFoundError:
		print("User not found.")
		exit()

def chop(user, padtype):
	"""Chop 200 bytes off of the pad."""
	try:
		usernumber = int(user) - 1
		user = getUser(usernumber, padtype)
	except ValueError:
		pass
	pad_bytes = bytearray(getPad(user, padtype))
	chopped_pad = pad_bytes[200:]
	with open('./{0}s/{1}'.format(padtype, user), 'wb') as f:
		f.write(chopped_pad)

def printPads(padtype = None):
	"""Print a list of pads, and return whether pads exists."""
	[inpads, outpads] = readPads()
	pad_exists = False
	
	if len(inpads) > 0 and padtype != 'outpad':
		pad_exists = True
		print("Inpads:")
		for pad in inpads:
			size = int(os.stat('./inpads/{0}'.format(pad)).st_size/200)
			print("\t{0}.) {1}\t\t{2} messages remaining.".format(inpads.index(pad) + 1, pad, size))
	
	if len(outpads) > 0 and padtype != 'inpad':
		pad_exists = True
		print("Outpads:")
		for pad in outpads:
			size = int(os.stat('./outpads/{0}'.format(pad)).st_size/200)
			print("\t{0}.) {1}\t\t{2} messages remaining.".format(outpads.index(pad) + 1, pad, size))
	
	return pad_exists

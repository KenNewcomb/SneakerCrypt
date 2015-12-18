""" pads.py: Reads/manipulates pads from ./pads """
import os

def readPads():
	"""Reads the pads from the filesystem."""
	inpads  = os.listdir('./inpads')
	outpads = os.listdir('./outpads')
	return [inpads, outpads]

def getPad(user, padtype):
	try:
		pad = open('./{0}s/{1}'.format(padtype, user), 'rb').read()
		return pad
	except FileNotFoundError:
		print("User not found.")
		exit()

def chop(user, padtype):
	"""Chop 200 bytes off of the pad."""
	pad_bytes = bytearray(getPad(user, padtype))
	chopped_pad = pad_bytes[200:]
	with open('./{0}s/{1}'.format(padtype, user), 'wb') as f:
		f.write(chopped_pad)

def printPads(padtype = None):
	[inpads, outpads] = readPads()
	
	if len(inpads) > 0 and padtype != 'outpad':
		print("Inpads:")
		for pad in inpads:
			size = int(os.stat('./inpads/{0}'.format(pad)).st_size/200)
			print("\t{0}.) {1}\t\t{2} messages remaining.".format(inpads.index(pad) + 1, pad, size))
	
	if len(outpads) > 0 and padtype != 'inpad':
		print("Outpads:")
		for pad in outpads:
			size = int(os.stat('./outpads/{0}'.format(pad)).st_size/200)
			print("\t{0}.) {1}\t\t{2} messages remaining.".format(outpads.index(pad) + 1, pad, size))

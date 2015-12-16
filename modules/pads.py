""" pads.py: Reads/manipulates pads from ./pads """
import os

def readPads():
	pads = os.listdir('./pads')
	return pads

def getPad(user):
	try:
		pad = open('./pads/{0}'.format(user), 'rb').read()
		print("Pad loaded successfully.")
		return pad
	except FileNotFoundError:
		print("User not found.")
		exit()

def printPads():
	pads = readPads()
	
	if len(pads) > 0:
		print("Stored Pads:")
	for pad in pads:
		# Calculate pad size
		size = str(os.stat('./pads/{0}'.format(pad)).st_size/1000.0)
		print("\t{0}.) {1}\t\t{2} KB".format(pads.index(pad) + 1, pad, size))
		

""" pads.py: Reads/manipulates pads from ./pads """
import os

def readPads():
	pads = os.listdir('./pads')
	return pads

def printPads():
	pads = readPads()
	if len(pads) > 0:
		print("Stored Pads:")
	for pad in pads:
		print("\t{0}.) {1}".format(pads.index(pad) + 1, pad))
		

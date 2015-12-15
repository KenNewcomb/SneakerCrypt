""" sneakercrypt.py: Encryption for the masses. """
__author = "Ken Newcomb"
import sys
from modules import pads, gen

def usage():
	print("Usage: python3 sneakercrypt.py <command>")
	print("Available Commands:")
	print("\t1.) pads     - View your stored pads.")
	print("\t2.) generate - Generate one-time-pad")
	print("\t3.) encrypt  - Encrypt message")
	print("\t4.) decrypt  - Decrypt message")
	exit()

# Sanitize input
if len(sys.argv) != 2:
	usage()

mode = sys.argv[1]

if mode == 'pads':
	pads.printPads()
elif mode == 'generate':
	gen.genPad()
elif mode is 'encrypt' or 'decrypt':
	pads.printPads()
	answer = input("Please choose a user: ")
	if mode is 'encrypt':
		crypto.encrypt(name, pad)
	else:
		crypto.decrypt(name, padd)
else:
	usage()

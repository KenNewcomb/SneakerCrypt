""" sneakercrypt.py: Encryption for the masses. """
__author = "Ken Newcomb"
import sys
from modules import pads, gen, crypto

def usage():
	logo()
	print("Usage: python3 sneakercrypt.py <command>")
	print("Available commands:")
	print("\t1.) pads     - View your stored pads.")
	print("\t2.) generate - Generate one-time-pad (outpad)")
	print("\t3.) encrypt  - Encrypt message")
	print("\t4.) decrypt  - Decrypt message\n")
	print("Pads:")
	print("\tinpads  - stored in ./inpads/  -  the location of received  pads, used to decrypt incoming messages.")
	print("\toutpads - stored in ./outpads/ -  the location of generated pads, used to encrypt outgoing messages.")
	exit()

def logo():
	print("""                         _                                      
   ()                   | |                                     
   /\  _  _    _   __,  | |   _   ,_    __   ,_           _ _|_ 
  /  \/ |/ |  |/  /  |  |/_) |/  /  |  /    /  |  |   | |/ \_|  
 /(__/  |  |_/|__/\_/|_/| \_/|__/   |_/\___/   |_/ \_/|/|__/ |_/
                                                     /|/|       
                                                     \|\|    """)
# Sanitize input
if len(sys.argv) != 2:
	usage()

# Get mode, take appropriate action
mode = sys.argv[1]
if mode == 'pads':
	pads.printPads()
elif mode == 'generate':
	gen.genPad()
elif mode == 'encrypt':
	pads.printPads('outpad')
	name = input("Please choose an outpad to encrypt your message: ")
	crypto.encrypt(pads.getPad(name, 'outpad'))
	pads.chop(name, 'outpad')
elif mode == 'decrypt':
	pads.printPads('inpad')
	name = input("Please choose an inpad to decrypt your message: ")
	crypto.decrypt(pads.getPad(name, 'inpad'))
	pads.chop(name, 'inpad')
else:
	usage()

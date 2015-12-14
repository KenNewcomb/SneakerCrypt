""" gen.py: Generate a one-time-pad. """
import random
import time
from sys import stdout

def userPrompt():
	"""Prompts the user for a bit of input regarding pad generation."""
	print("How many kilobytes of random numbers would you like to generate?")
	print("   10 kilobytes =    25 messages (\"The Quick Update\")")
	print("  100 kilobytes =   250 messages (\"The Conversation\")")
	print(" 1000 kilobytes =  2500 messages (\"Some Discussions\")")
	print("10000 kilobytes = 25000 messages (\"Social Butterfly\")")
	num_kb = int(input("Generate (kilobytes) :  "))
	if num_kb > 50:
		time = (num_kb/2.0)/60.0
		answer = input("Generating {0} kilobytes will require approximately {1:.1f} minutes. Continue? (Y/n) ".format(num_kb, time))
		if answer.lower() == "n":
			print("Sneakercrypt has terminated.")
			exit()
	name = input("Please enter a name associated with this key: ")
	return [name, num_kb]
	
def getPad(numKiloBytes):
	pad = ""
	for i in range(1,numKiloBytes):
		part = random.randint(0,2**(8000) -1)
		pad += str(part)
		print("Generated " + str(i) + " kilobytes. " + str(int(100*i/numKiloBytes)) + "% complete.")
	return pad

def savePad(name, pad):
	"""Saves pad to disk."""
	with open('./pads/{0}'.format(name), 'w') as f:
		f.write(pad)

def genPad():
	"""Generates a one-time pad."""
	# Prompt the user for input
	user_input = userPrompt()
	name   = user_input[0]
	num_kb = user_input[1]
	
	# Generate a pad of length num_kb
	pad = getPad(num_kb)
	
	# Save the pad to disk.
	savePad(name, pad)

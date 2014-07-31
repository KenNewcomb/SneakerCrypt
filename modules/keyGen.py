import random
import time
from sys import stdout

def get(numbits):
	return random.randint(0, 2**numbits -1)

def getPad(numKiloBytes):
	key = 0
	for i in range(1,numKiloBytes):
		part = random.randint(0,2**(8000) -1)
		key = int(str(key) + str(part))
		print("Generated " + str(i) + " kilobytes. " + str(int(100*i/numKiloBytes)) + "% complete.")
	return key

def writePad(path, filename, key):
	padfile = open(path+filename, 'w')
	padfile.write((str(key)))		

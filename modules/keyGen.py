from random import SystemRandom
import time

def get(numbits):
	seed = time.time()
	r1 = SystemRandom(seed)
	return r1.randint(0, 2**numbits -1)

def getPad(numKiloBytes):
	seed = time.time()
	r1 = SystemRandom(seed)
	key = 0
	for i in range(1,numKiloBytes):
		part = r1.randint(0,2**(8000) -1)
		key = int(str(key) + str(part))
		print("Generated " + str(i) + " kilobytes")
	print(key)

from random import SystemRandom
import time

def get(numbits):
	seed = time.time()
	r1 = SystemRandom(seed)
	return r1.randint(0, 2**numbits -1)

def getPad():
	return

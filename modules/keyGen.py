import random

def get(numbits):
	print("".join(str(random.SystemRandom.randint(0,1) for i in range(numbits))))

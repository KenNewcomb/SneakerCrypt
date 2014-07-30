from classes.message import Message
from modules import keyGen

## Current demonstration of functionality:

# The program will take any string as an input. 
# It will convert the unicode string to binary, pad the message,
# generate a random key, encrypt the message against the pad,
# decrypt the message against the pad, depad the message,
# and finally convert the message back to readable strings. 

input_message = input("Input a message:")
sample_message = Message(input_message)

# Encryption
sample_message.toBinary()
print("message after binary=\n" + repr(sample_message))
sample_message.pad()
print("message after padding=\n" + repr(sample_message))
key = keyGen.get(len(repr(sample_message)))
print("key:\n" + bin(key))
sample_message.encrypt(key)
print("encrypted message:\n" + repr(sample_message))

# Decryption
sample_message.decrypt(key)
print("decrypted message:\n" + repr(sample_message))
sample_message.depad()
print("depadded message:\n" + repr(sample_message))
sample_message.toString()
print("plaintext:\n" + repr(sample_message))

print(keyGen.getPad(30))

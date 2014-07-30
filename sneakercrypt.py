from classes.message import Message
from modules import keyGen

## Current demonstration of functionality:
input_message = input("Input a message:")
sample_message = Message(input_message)

# Encryption
sample_message.toBinary()
sample_message.pad()
print("message after padding=\n" + repr(sample_message))
key = keyGen.get(len(repr(sample_message)))
print("key:\n" + bin(key))
sample_message.encrypt(key)
print("encrypted message:\n" + repr(sample_message))

# Decryption
sample_message.decrypt(key)
print("decrypted message:\n" + repr(sample_message))
sample_message.decode()
print("decoded message:\n" + repr(sample_message))

from classes.message import Message
from modules import keyGen

## Current demonstration of functionality:
input_message = input("Input a message:")
sample_message = Message(input_message)


# Encryption
sample_message.toBinary()
sample_message.pad()
key = keyGen.get(len(sample_message.message))
print(key)
sample_message.encrypt(key)
print(sample_message.message)
# Decryption


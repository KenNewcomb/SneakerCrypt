from classes.message import Message

## Current demonstration of functionality:
input_message = input("Input a message:")
sample_message = Message(input_message)
key = input("Input a key:")

sample_message.toBinary()
sample_message.pad()

sample_message.encrypt(sample_message.message)

key = input("Input the key to decrypt")



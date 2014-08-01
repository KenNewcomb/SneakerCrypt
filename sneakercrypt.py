from classes.message import Message
from modules import keyGen
from classes.database import Database
## Current demonstration of functionality (uncomment either section)

# The program will take any string as an input. 
# It will convert the unicode string to binary, pad the message,
# generate a random key, encrypt the message against the pad,
# decrypt the message against the pad, depad the message,
# and finally convert the message back to readable strings. 
"""
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

"""
"""
# This part of the program generates a 25kb pad, and writes the pad to a file.

pad = keyGen.getPad(25) # of kilobytes
print(pad)
id = 1
keyGen.writePad("/home/mango/Projects/SneakerCrypt/keys/", str(id), key)
"""

# User database functionality:
db = Database()
db.makeUserTable()
db.addUser("Ken", 0,0,'somestring','anotherstring')
db.printUsers()
db.removeUser("Ken")

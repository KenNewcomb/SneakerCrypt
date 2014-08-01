from classes.message import Message
from modules import keyGen
from classes.database import Database

######################################################################
# Current demonstration of functionality (uncomment desired section) #
######################################################################

# The program will take any string as an input, encrypt it with a random pad,
# and decrypt with the same pad. 

'''
input_message = input("Input a message:")
sample_message = Message(input_message)

# Encryption
sample_message.toBinary()
sample_message.pad()
key = keyGen.get(len(repr(sample_message))) # Generate a random key the length of the message
sample_message.encrypt(key)
print("encrypted message:\n" + repr(sample_message))

# Decryption
sample_message.decrypt(key)
sample_message.depad()
sample_message.toString()
print("plaintext:\n" + repr(sample_message))
'''

# This part of the program generates a 25kb pad, and writes the pad to a file.
'''
pad = keyGen.getPad(25) # of kilobytes
print(pad)
id = 1
keyGen.writePad("/home/mango/Projects/SneakerCrypt/keys/", str(id), key)
'''

# User database functionality (in progress)

db = Database()
db.makeUserTable()
db.addUser("Ken")
db.printUsers()
db.addUserKey("Ken", "path_to_keyfile")
db.printUsers()

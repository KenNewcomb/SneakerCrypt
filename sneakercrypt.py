from modules import crypto

## Current demonstration of functionality:
message = input("Input a message:")
key = input("Input a key:")

print("message =" + message)
print("message length=" + str(len(message)))

binary_string = crypto.messageToBinary(message)
print("binary =" + binary_string)
print("binary length=" + str(len(binary_string)))

padded_message = crypto.padMessage(binary_string)
print("padded message=" + padded_message)
print("padded message length=" + str(len(padded_message)))
# for the purpose of example, the key will be generated as such:
key = crypto.messageToBinary(key)
key = crypto.padMessage(key)

cyphertext = crypto.encrypt(key,padded_message)
print("cyphertext=" + cyphertext)
print("cyphertext length=" + str(len(cyphertext)))

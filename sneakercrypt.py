from modules import crypto

message = "Hi! I want a peanut butter cookie"
binary = crypto.messageToBinary(message)
print binary
padded_message = crypto.padMessage(binary)
print padded_message

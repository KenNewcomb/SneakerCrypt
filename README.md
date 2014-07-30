# SneakerCrypt
Sneakercrypt is a project focused on creating a chat client with easy-to-use OTP encryption. More to come.

### Project Goals
1. Implement cryptographic functions with tests.
2. Implement functionality to write a large, random key to a USB

### Design Considerations
1. How should the system securely generate random numbers suitable for cryptography?
   os.urandom() is suitable for cryptography. An option for using a physical RNG will be considered.

2. How large should a key be?
   64MB may be sufficient. A key this size will take a few minutes to generate.

### Project Updates:
+ 07/30/2014 - Working encryption/decryption.

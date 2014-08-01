# SneakerCrypt
Sneakercrypt is easy-to-use chat software that implements the theoretically secure [one-time-pad encryption scheme](https://en.wikipedia.org/One_Time_Pad).

### Project Goals
1. Implement cryptographic functions with tests.
2. Implement functionality to write a large, random key to a USB

### Design Considerations
1. How should the system securely generate random numbers suitable for cryptography?

   os.urandom() is suitable for cryptography. An option for using a physical RNG will be considered.

2. How large should a key be?

   64MB may be sufficient. A key this size will take a few minutes to generate.
   UPDATE: A key this size will take significantly longer to generate on most platforms.
   This option will be left for the user to decide.

3. GUI?

   I am currently looking into Flask for developing a web interface.

### Project Updates:
+ 08/01/2014 - Database development in progress
+ 07/30/2014 - Started front-end interface development
+ 07/30/2014 - Working encryption/decryption.

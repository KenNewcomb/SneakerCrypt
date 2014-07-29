import unittest
from modules import crypto

class cryptoTest(unittest.TestCase):

	def test_message_to_binary(self):
		binary = crypto.messageToBinary("hello")
		self.assertEqual("10111101010110111101101100100011100101101001111",binary)

if __name__ == '__main__':
	unittest.main()

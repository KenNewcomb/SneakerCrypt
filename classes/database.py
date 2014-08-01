import sqlite3

class Database:

	def __init__(self):
		"""Initialize a SQLite3 Database."""
		self.db = sqlite3.connect('/home/mango/Projects/SneakerCrypt/userdata/userdb')

	def databaseClose(self):
		self.db.close()

	def databaseExists(self):
		cursor = self.db.cursor()
		result = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='table_name';""") 
		if cursor.fetchall() == []: # no table exists
			return False
		else:
			return True

	def addUser(username, pad1 = '', pad2 = ''):
		cursor = self.db.cursor()

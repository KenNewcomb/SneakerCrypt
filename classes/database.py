import sqlite3

class Database:

	def __init__(self):
		"""Initialize a SQLite3 Database."""
		self.db = sqlite3.connect('/home/mango/Projects/SneakerCrypt/userdata/userdb')

	def databaseClose(self):
		self.db.close()

	def makeUserTable(self):
		cursor = self.db.cursor()
		result = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='users';""") 
		if cursor.fetchall() == []: # no table exists
			return cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)''')

	def addUser(username, pad1 = '', pad2 = ''):
		cursor = self.db.cursor()
		db.commit()
		

import sqlite3

class Database:

	def __init__(self):
		'''Initialize a SQLite3 Database.'''
		self.db = sqlite3.connect('/home/mango/Projects/SneakerCrypt/userdata/userdb')

	def close(self):
		self.db.close()

	def makeUserTable(self):
		'''Create a table for users if one doesn't already exist.'''
		cursor = self.db.cursor()
		result = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='users';""") 
		if cursor.fetchall() == []: # no table exists
			cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, muser1 INTEGER, muser2 INTEGER, paduser1 TEXT, paduser2 TEXT)''')
			self.db.commit()

	def addUser(self,username):
		'''Adds a user to the database.'''
		cursor = self.db.cursor()
		cursor.execute('''INSERT INTO users(username) VALUES(?)''', (username,))
		self.db.commit()

	def removeUser(self,username):
		'''Removes a user from the database.'''
		cursor = self.db.cursor()
		cursor.execute('''DELETE FROM users WHERE username = ?''', (username,))
		self.db.commit()

	def printUsers(self):
		'''Print all users in the user table'''
		cursor = self.db.cursor()
		cursor.execute('''SELECT * FROM users''')
		users = cursor.fetchall()
		for user in users:
			for column in user:
				print(column)
	
	def addUserKey(self, username, path):
		'''Adds the key associated with the messages SENT BY THE USER to "username"'''
		cursor = self.db.cursor()
		cursor.execute('''UPDATE users SET paduser1 = ? WHERE username = ? ''', (path, username,))
		self.db.commit()

	def addContactKey(self, username, path):
		'''Adds the key associated with the messages SENT BY THE CONTACT, "username"'''
		cursor = self.db.curson()
		cursor.execute('''UPDATE users SET paduser2 = ? WHERE username = ? ''', (path, username))

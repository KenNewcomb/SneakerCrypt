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
			cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, muser1 INTEGER, muser2 INTEGER, paduser1 TEXT, paduser2 TEXT)''')
			self.db.commit()

	def addUser(self,username, muser1 = 0, muser2 = 0, paduser1 = '', paduser2 = ''):
		"""Adds a user to the database."""
		cursor = self.db.cursor()
		cursor.execute('''INSERT INTO users(username, muser1, muser2, paduser1, paduser2) VALUES(?,?,?,?,?)''', (username, muser1, muser2, paduser1, paduser2))
		print("Username: " + username + " added to database")
		self.db.commit()

	def removeUser(self,username):
		cursor = self.db.cursor()
		cursor.execute('''DELETE FROM users WHERE username = ?''', (username,))
		print("Username: " + username + " deleted")
		self.db.commit()

	def printUsers(self):
		"""Print all users in the table"""
		cursor = self.db.cursor()
		cursor.execute('''SELECT username FROM users''')
		users = cursor.fetchall()
		for user in users:
			print(user[0])

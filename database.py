import sqlite3
from sqlite3 import Error

class database:
	def __init__(self, name, dbfile="data.db"):
		self.name = name
		self.conn = None
		self.dbfile = dbfile

	def connect(self):
		try:
			self.conn = sqlite3.connect(self.dbfile)
			self.c = self.conn.cursor()
			self.c.execute()
		except Error as e:
			print(e)
		finally:
			if conn:
				conn.close
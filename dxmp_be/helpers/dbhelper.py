from functools import wraps

from flask import current_app
from flaskext.mysql import MySQL

mysql = MySQL()

class DBInterface:
	def __init__(self):
		self.mysql = current_app.mysql
		self.cursor = self.mysql.get_db().cursor()

	def query_db(self, query):
		self.cursor.execute(query)
		return self.cursor.fetchall()

	def close_db(error):
		if hasattr(g, 'mysql_db'):
			#g.mysql_db.close()
			pass

def hydrate_db_results(list, params):
	paramCount = len(params)
	return [{params[x]: val[x] for x in xrange(paramCount)} for val in list]

def uses_db(function):
	@wraps(function)
	def wrapper(*args, **kwargs):
		dbi = DBInterface()
		return function(db=dbi, *args, **kwargs)
	return wrapper
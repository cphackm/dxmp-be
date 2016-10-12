from functools import wraps

from flask import current_app
from flaskext.mysql import MySQL

mysql = MySQL()

class DBInterface:
	"""
	Provides access to the underlying MySQL database.
	"""
	def __init__(self):
		self.mysql = current_app.mysql
		self.cursor = self.mysql.get_db().cursor()

	def query_db(self, query):
		"""
		Runs a query and returns the result.

		args:
		query -- A query to run on the database.

		returns: Raw results from the given query.
		"""
		self.cursor.execute(query)
		return self.cursor.fetchall()

def hydrate_db_results(list, params):
	"""
	Hydrates raw database results by providing keys for column values.

	args:
	list	-- A list of lists containing results to hydrate.
	params	-- A list of string to attach as keys to the data in list.

	returns: Hydrated database results as a list of dictionaries.
	"""
	paramCount = len(params)
	return [{params[x]: val[x] for x in xrange(paramCount)} for val in list]

def uses_db(function):
	"""
	A decorator providing a reference to the current database connection.

	Functions using this decorator must have 'db' as one of their args.
	"""
	@wraps(function)
	def wrapper(*args, **kwargs):
		dbi = DBInterface()
		return function(db=dbi, *args, **kwargs)
	return wrapper
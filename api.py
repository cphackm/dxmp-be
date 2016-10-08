from flask import Flask, g, request, jsonify
from flaskext.mysql import MySQL

import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read('config.ini')

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
	MYSQL_DATABASE_DB=Config.get('MySQL', 'Database'),
	MYSQL_DATABASE_USER=Config.get('MySQL', 'User'),
	MYSQL_DATABASE_PASSWORD=Config.get('MySQL', 'Password')
))

mysql = MySQL()
mysql.init_app(app)

SONG_SCHEMA = [
	'id', 
	'title', 
	'album_id', 
	'artist_id', 
	'filename', 
	'duration', 
	'track', 
	'disc', 
	'year', 
	'created', 
	'added_by'
]

ALBUM_SCHEMA = [
	'id',
	'title',
	'art',
	'wallpaper'
]

def get_db():
	if not hasattr(g, 'mysql_db'):
		g.mysql_db = mysql.get_db()
	return g.mysql_db

@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'mysql_db'):
		#g.mysql_db.close()
		pass

def query_db(query):
	cursor = get_db().cursor()
	cursor.execute(query)
	return cursor.fetchall()

@app.route("/songs")
def get_songs():
	rawEntries = query_db('select * from songs')
	entries = hydrate_db_results(
		rawEntries,
		SONG_SCHEMA
	)
	return jsonify(entries)

@app.route("/albums")
def get_albums():
	rawEntries = query_db('select * from albums')
	entries = hydrate_db_results(
		rawEntries, 
		ALBUM_SCHEMA
	)
	return jsonify(entries)

def hydrate_db_results(list, params):
	paramCount = len(params)
	return [{params[x]: val[x] for x in xrange(paramCount)} for val in list]

if __name__ == "__main__":
	app.run()

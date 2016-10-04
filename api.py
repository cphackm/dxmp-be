from flask import Flask, g, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
	MYSQL_DATABASE_USER='root',
	MYSQL_DATABASE_DB='dxmp'
))

mysql = MySQL()
mysql.init_app(app)

def get_db():
	if not hasattr(g, 'mysql_db'):
		g.mysql_db = mysql.get_db()
	return g.mysql_db

@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'mysql_db'):
		#g.mysql_db.close()
		pass

@app.route("/songs")
def get_songs():
	cursor = get_db().cursor()
	cursor.execute('select * from songs')
	entries = cursor.fetchall()
	return jsonify(entries)

if __name__ == "__main__":
	app.run()
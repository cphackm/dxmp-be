import ConfigParser

from flask import Flask, g, request, jsonify
from flaskext.mysql import MySQL

from api.content import content_api

Config = ConfigParser.ConfigParser()
Config.read('config.ini')

app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)
app.mysql = mysql

app.register_blueprint(content_api)
app.config.from_object(__name__)

app.config.update(dict(
	MYSQL_DATABASE_DB=Config.get('MySQL', 'Database'),
	MYSQL_DATABASE_USER=Config.get('MySQL', 'User'),
	MYSQL_DATABASE_PASSWORD=Config.get('MySQL', 'Password')
))

if __name__ == "__main__":
	app.run()

from flask import Flask, Blueprint, g, request, jsonify, current_app

from dxmp_be.helpers.dbhelper import DBInterface, uses_db, hydrate_db_results
from hydration_info import SONGS_SCHEMA, ALBUMS_SCHEMA

content_api = Blueprint('api', __name__)

@content_api.route('/api/content/songs')
@uses_db
def get_songs(db):
	"""
	Queries the database for all songs.

	returns: A hydrated list of songs represented as dictionaries.
	"""
	rawEntries = db.query_db('select * from songs')
	entries = hydrate_db_results(
		rawEntries,
		SONGS_SCHEMA
	)
	return jsonify(entries)

@content_api.route("/api/content/albums")
@uses_db
def get_albums(db):
	"""
	Queries the database for all albums.

	returns: A hydrated list of songs represented as dictionaries.
	"""
	rawEntries = db.query_db('select * from albums')
	entries = hydrate_db_results(
		rawEntries, 
		ALBUMS_SCHEMA
	)
	return jsonify(entries)
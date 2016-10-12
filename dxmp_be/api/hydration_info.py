ALBUMS_SCHEMA = [
	'id',
	'title',
	'art',
	'wallpaper'
]
ARTISTS_SCHEMA = [
	'id',
	'name'
]
PLAYLIST_SONGS_SCHEMA = [
	'playlist_id',
	'song_id'
]
PLAYLISTS_SCHEMA = [
	'id',
	'name',
	'user_id',
	'created'
]
SONGS_SCHEMA = [
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
TAGS_SCHEMA = [
	'song_id',
	'tag'
]
TRACKING_SCHEMA = [
	'song_id',
	'type',
	'user_id',
	'date'
]
USERS_SCHEMA = [
	'id',
	'name',
	'password',
	'email'
]

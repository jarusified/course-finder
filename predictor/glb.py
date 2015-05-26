import os

def _get_api_key(key):
	try:
		return os.environ[key]
	except KeyError:
		return None

API_KEY = _get_api_key('TMDB_API');

###VARIALBES

MOVIENAME='The Dark Knight'
departments=['Sound','Camera','Costume & Make-Up','Crew','Directing','Writing','Visual Effects','Production','Art','Editing']

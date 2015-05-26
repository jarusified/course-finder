import tmdbsimple as tmdb
from glb import *

def getMovieData(movieName):
	search=tmdb.Search()
	responses=search.movie(query=movieName)
	movie=tmdb.Movies(responses['results'][0]['id'])
	return movie

def movieSearch(movieName):
	movie=getMovieData(movieName);
	info=movie.info()
	return info

def helperSearch(movieName,answer,answerDepartment):
	movie=getMovieData(movieName);
	info=movie.info()
	credits=movie.credits()[answerDepartment]
	answerId=[]

	if(answer=='Directing' or answer=='Production'):
		for i in range(len(credits)):	
			if(credits[i]['department']==answer):
				answerId.append(credits[i]['id'])
		return answerId[0:3]			
	
	else:
		for i in range(len(credits)):	
			answerId.append(credits[i]['id'])

	
	return answerId[0:3]		

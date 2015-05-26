# Predicting sucess of movie.

## Requirements
 * Install tmdb [tmdbsimple]( https://pypi.python.org/pypi/tmdbsimple ) 
 * export TMDB_API="API_KEY"


## Features 
 * Check features.txt.

## Running 
 * Change movie name in the globals glb.py
    ```
	 python predictor/sample.py 
    ```

## Output
 * Fetches ids of director,producer and actors in the movie.

## To Do :
 * Fetch movie budget,revenue of this movie.
 * Fetch the average budgets,revenue,rating of previous movies by this director,producer,actor.
 * Adjust all cost factors by including in inflation factor.
 * Come up with more input Features.
 * The more data ,the better the results.
 * Form the input Feature Vector.
 * The target Vector is the revenue,rating of a new movie .
 *  Create models and predict for new movies.

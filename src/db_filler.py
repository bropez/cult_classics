import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

import django
django.setup()

from films.models import Actor, Genre, Director, Movie, Writer

if __name__ == "__main__":
    json_file = open('../json/movies_formatted.json')
    json_str = json_file.read()
    json_data = json.loads(json_str)

    for obj in json_data:
        movie_name = obj['title']
        movie_year = obj['year']
        movie_runtime = 0
        if 'runtimes' in obj.keys():
            movie_runtime = int(obj['runtimes'][0])
        if 'rating' in obj.keys():
            movie_rating = float(obj['rating'])
        movie_thumbnail_url = "Not found"
        if 'cover url' in obj.keys():
            movie_thumbnail_url = obj['cover url']
        movie_cover_url = "Not found"
        if 'full-size cover url' in obj.keys():
            movie_cover_url = obj['full-size cover url']
        movie_plot_outline = "Not found"
        if 'plot outline' in obj.keys():
            movie_plot_outline = obj['plot outline']

        movie_cast = set()
        movie_directors = set()
        movie_writers = set()
        movie_genres = set()
        if 'cast' in obj.keys():
            for person in obj['cast']:
                movie_cast.add(person)
        if 'directors' in obj.keys():
            for person in obj['directors']:
                movie_directors.add(person)
        if 'writer' in obj.keys():
            for person in obj['writers']:
                if person == "":
                    continue
                else:
                    movie_writers.add(person)
        if 'genres' in obj.keys():
            for genre in obj['genres']:
                movie_genres.add(genre)

        # adding the actors, directors, genres
        print("Creating movie: " + movie_name)
        my_movie = Movie.objects.get_or_create(name=movie_name, year=movie_year, runtime=movie_runtime,
                                               rating=movie_rating, thumbnail_url=movie_thumbnail_url,
                                               cover_url=movie_cover_url, plot_outline=movie_plot_outline)[0]
        print("Successfully created movie: " + movie_name)

        print("Adding Actors: ")
        for actor_name in movie_cast:
            actor = Actor.objects.get_or_create(name=actor_name)[0]
            my_movie.cast.add(actor)
            print("Added " + actor_name)
        print("Added all actors to: " + movie_name)

        print("Adding Directors: ")
        for director_name in movie_directors:
            director = Director.objects.get_or_create(name=director_name)[0]
            my_movie.directors.add(director)
            print("Added " + director_name)
        print("Added all directors to: " + movie_name)

        print("Adding Writers: ")
        for writer_name in movie_writers:
            writer = Writer.objects.get_or_create(name=writer_name)[0]
            my_movie.writers.add(writer)
            print("Added " + writer_name)
        print("Added all writers to: " + movie_name)

        print("Adding Genres: ")
        for genre_name in movie_genres:
            genre = Genre.objects.get_or_create(name=genre_name)[0]
            my_movie.genres.add(genre)
            print("Added " + genre_name)
        print("Added all genres")
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.
# sncy: when 127.0.0.1:8000/movies is requested, index() is going to get called.
# sncy: every view function should return http response


def index(request):
    # sncy: SELECT * FROM movies_movie
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

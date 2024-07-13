from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie
# Create your views here.

def index(request):
    movies = Movie.objects.order_by('genre') ## SELECT * FROM 
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))

def movie(request, movie_id):
    #SELECT * FROM movie_movie WHERE id='movie_id'
    pokemon = Movie.objects.get(id=movie_id)
    template = loader.get_template('display_movie.html')
    context = {
        'movie': movie 
    }
    return HttpResponse(template.render(context, request))
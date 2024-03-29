from django.shortcuts import render
from .models import Movie

def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()

    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html', {'template_data': template_data})

def show(request, id):
    movie = Movie.objects.get(id=id)

    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    return render(request, 'movies/show.html', {'template_data': template_data})
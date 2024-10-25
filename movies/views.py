from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        'movies': ['gladiator', 'top gun', 'forest gump']

    }
    return render(request, 'movies/index.html', context)

# app/template/app/index.html
# movies/templates/movies/index.html


def about(request):
    return render(request, 'movies/about.html', {})

from django.shortcuts import render, HttpResponse, redirect
from .models import Movies, MovieImage

# Create your views here.


def home(request):
    return HttpResponse("Helloworld")


def index(request):
    name = "Vybhi"
    return render(request, 'home.html', {'name': name})


def display_movie(request):
    movies = Movies.objects.all()
    return render(request, "display_movies.html", {'movies': movies})


def movies_input(request):
    if request.method == 'GET':
        return render(request, 'movies_input.html')
    elif request.method == 'POST':
        movie = request.POST['movie']
        language = request.POST['language']
        year = request.POST['year']
        Movies(movie_name=movie, language=language, year=year).save()
        return render(request, 'movies_input.html', {'status': 'Data inserted successfully'})


def delete_record(request, id):
    obj = Movies.objects.get(id=id)
    obj.delete()
    #return HttpResponse(f"Your selected id={obj.movie_name}")
    return redirect('display-movies')


def update_record(request, id):
    obj = Movies.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'update_movies.html', {'movie': obj})
    elif request.method == 'POST':
        obj.movie_name = request.POST['movie']
        obj.language = request.POST['language']
        obj.year = request.POST['year']
        obj.save()
        return redirect('display-movies')


def show_images(request, id):
    obj = Movies.objects.get(id=id)
    return render(request, 'showimages.html', {'movie': obj})


def insert_image(request, id):
    obj = Movies.objects.get(id=id)
    if request.method == 'GET':
        return render(request,'insert_image.html', {'movie':obj})
    elif request.method == 'POST':
        image_url = request.POST['image-url']
        MovieImage(image_url=image_url, movie=obj).save()
        return render(request, 'insert_image.html', {'movie': obj})
    return redirect("display-movies")
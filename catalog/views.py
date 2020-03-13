from django.shortcuts import render
from .models import Book, Author, Genre, Language, BookInstance


def index(request):
    """
    View function for index page.
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_harry_books = Book.objects.all().filter(title__icontains='harry').count()

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_harry_books': num_harry_books,
        }
    )


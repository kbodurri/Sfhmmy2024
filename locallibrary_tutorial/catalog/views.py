from .models import Book, Author, BookInstance, Genre

from django.views import generic
from django.shortcuts import render

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'authors/author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/author_detail.html'

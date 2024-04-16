from django.core.management.base import BaseCommand
from django.utils import timezone
from catalog.models import Genre, Book, BookInstance, Author, Language


def create_genre(name):
    genre, created = Genre.objects.update_or_create(
        name__iexact=name,
        defaults={'name': name}
    )
    if created:
        print(f'Created Genre: {name}')
    else:
        print(f'Genre already exists: {name}')
    return genre


def create_language(name):
    language, created = Language.objects.update_or_create(
        name__iexact=name,
        defaults={'name': name}
    )
    if created:
        print(f'Created Language: {name}')
    else:
        print(f'Language already exists: {name}')
    return language


def create_author(first_name, last_name, birth_date, death_date):
    author, created = Author.objects.update_or_create(
        first_name__iexact=first_name,
        last_name__iexact=last_name,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': birth_date,
            'date_of_death': death_date
        }
    )
    if created:
        print(f'Created Author: {first_name} {last_name}')
    else:
        print(f'Author already exists: {first_name} {last_name}')
    return author


def create_book(title, author, summary, isbn, language, genres):
    book, created = Book.objects.update_or_create(
        title__iexact=title,
        author=author,
        defaults={
            'title': title,
            'author': author,
            'summary': summary,
            'isbn': isbn,
            'language': language
        }
    )
    if created:
        book.genre.set(genres)
        print(f'Created Book: {title}')
    else:
        print(f'Book already exists: {title}')
    return book


def create_book_instance(book, imprint, due_back, status):
    instance, created = BookInstance.objects.update_or_create(
        book=book,
        imprint=imprint,
        defaults={
            'book': book,
            'imprint': imprint,
            'due_back': due_back,
            'status': status
        }
    )
    if created:
        print(f'Created Book Instance: {book.title}')
    else:
        print(f'Book Instance already exists: {book.title}')
    return instance


def generate_sample_data():
    # Create Genres
    genre_sf = create_genre('Science Fiction')
    genre_fantasy = create_genre('Fantasy')
    genre_mystery = create_genre('Mystery')

    # Create Languages
    language_english = create_language('English')
    language_french = create_language('French')

    # Create Authors
    author_orwell = create_author('George', 'Orwell', '1903-06-25', '1950-01-21')
    author_tolkien = create_author('J.R.R.', 'Tolkien', '1892-01-03', '1973-09-02')
    author_christie = create_author('Agatha', 'Christie', '1890-09-15', '1976-01-12')

    # Create Books
    book_1984 = create_book(
        '1984',
        author_orwell,
        'A dystopian novel set in a totalitarian regime.',
        '978-0451524935',
        language_english,
        [genre_sf]
    )

    book_animal_farm = create_book(
        'Animal Farm',
        author_orwell,
        'A political allegory featuring farm animals.',
        '978-0451526342',
        language_english,
        [genre_fantasy]
    )

    book_lotr = create_book(
        'The Lord of the Rings',
        author_tolkien,
        'Epic fantasy adventure.',
        '978-0544003415',
        language_english,
        [genre_fantasy]
    )

    book_hobbit = create_book(
        'The Hobbit',
        author_tolkien,
        'The adventure of Bilbo Baggins.',
        '978-0345339683',
        language_english,
        [genre_fantasy]
    )

    book_orient_express = create_book(
        'Murder on the Orient Express',
        author_christie,
        'A famous detective investigates a murder on a train.',
        '978-0062693662',
        language_english,
        [genre_mystery]
    )

    book_murder_nile = create_book(
        'Death on the Nile',
        author_christie,
        'Hercule Poirot solves a murder on a cruise.',
        '978-0062073556',
        language_english,
        [genre_mystery]
    )

    # Create Book Instances
    create_book_instance(
        book_1984,
        'Penguin Books',
        timezone.now() + timezone.timedelta(days=30),
        'a'
    )

    create_book_instance(
        book_animal_farm,
        'Signet Classics',
        timezone.now() + timezone.timedelta(days=20),
        'a'
    )

    create_book_instance(
        book_lotr,
        'Mariner Books',
        timezone.now() + timezone.timedelta(days=40),
        'a'
    )

    create_book_instance(
        book_hobbit,
        'Houghton Mifflin Harcourt',
        timezone.now() + timezone.timedelta(days=25),
        'a'
    )

    create_book_instance(
        book_orient_express,
        'HarperCollins',
        timezone.now() + timezone.timedelta(days=35),
        'a'
    )

    create_book_instance(
        book_murder_nile,
        'William Morrow Paperbacks',
        timezone.now() + timezone.timedelta(days=30),
        'a'
    )


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        generate_sample_data()
        self.stdout.write(self.style.SUCCESS('Sample data created successfully.'))

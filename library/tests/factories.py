import factory

from ..models import Book, BorrowRecord

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Sequence(lambda n: f'title{n}')
    author = factory.Sequence(lambda n: f'author{n}')


class BorrowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BorrowRecord

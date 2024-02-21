import pytest

@pytest.fixture(scope='class') 
@pytest.mark.django_db
def test_book_factory(book_factory):
   book = book_factory()
   assert book.title == 'title0'


@pytest.fixture(scope='class')
@pytest.mark.django_db
def test_borrow_records_factory(book_factory, borrow_factory, user_factory):
   book = book_factory()
   user = user_factory()
   borrow_record = borrow_factory(book = book, borrower = user)
   assert borrow_record.book.title == book.title


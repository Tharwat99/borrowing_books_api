from . models import Book, BorrowRecord
import django_filters

class BookListFilter(django_filters.FilterSet):
    """ 
    filter book using title, author, and is_available
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Book
        fields = ["title", "author", "is_available"]
        order_by = ['-id', 'id','-title', 'title', '-author', 'author']

class BorrowRecordListFilter(django_filters.FilterSet):
    """ 
    filter borrow record using book, borrower, borrow_date, and return_date
    """
    class Meta:
        model = BorrowRecord
        fields = ["book", "borrower", "borrow_date", "return_date"]
        order_by = ['-id', 'id','-borrow_date', 'borrow_date', '-return_date', 'return_date']
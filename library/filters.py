from . models import BorrowRecord
import django_filters

class BorrowRecordListFilter(django_filters.FilterSet):
    """ 
    filter borrow record using book, borrower, borrow_date, and return_date
    """
    class Meta:
        model = BorrowRecord
        fields = ["book", "borrower", "borrow_date", "return_date"]
        order_by = ['-id', 'id','-borrow_date', 'borrow_date', '-return_date', 'return_date']
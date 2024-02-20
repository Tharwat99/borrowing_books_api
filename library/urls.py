from django.urls import path
from library.views import BookCreateView, BookListView, BookRetrieveView, BorrowRecordCreateView, BorrowRecordListView, BorrowRecordRetrieveUpdateView

urlpatterns = [
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/list/', BookListView.as_view(), name='book-list'),
    path('books/details/<int:pk>/', BookRetrieveView.as_view(), name='book-details'),
    path('borrow-records/create/', BorrowRecordCreateView.as_view(), name='borrow-book'),
    path('borrow-records/list/', BorrowRecordListView.as_view(), name='borrow-records-list'),
    path('borrow-records/details/<int:pk>/', BorrowRecordRetrieveUpdateView.as_view(), name='borrow-records-details')
]
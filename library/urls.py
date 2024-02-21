from django.urls import path
from library.views import (
    BookCreateView, 
    BookListView, 
    BookRetrieveView,
    BookUpdateView,
    BorrowRecordCreateView, 
    BorrowRecordListView,
    BorrowRecordUpdateView,
    BorrowRecordRetrieveView
)

urlpatterns = [
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/list/', BookListView.as_view(), name='book-list'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/retrieve/<int:pk>/', BookRetrieveView.as_view(), name='book-retrieve'),
    path('borrow-records/create/', BorrowRecordCreateView.as_view(), name='borrow-book'),
    path('borrow-records/list/', BorrowRecordListView.as_view(), name='borrow-records-list'),
    path('borrow-records/update/<int:pk>/', BorrowRecordUpdateView.as_view(), name='borrow-records-update'),
    path('borrow-records/retrieve/<int:pk>/', BorrowRecordRetrieveView.as_view(), name='borrow-records-retrieve')

]
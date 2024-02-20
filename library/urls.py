from django.urls import path
from library.views import BookListView, BookRetrieveView, BorrowRecordCreateView, BorrowRecordListView, BorrowRecordRetrieveUpdateView

urlpatterns = [
    path('books-list/', BookListView.as_view(), name='book-list'),
    path('books-details/<int:pk>/', BookRetrieveView.as_view(), name='book-details'),
    path('borrow-book/', BorrowRecordCreateView.as_view(), name='borrow-book'),
    path('borrow-records/', BorrowRecordListView.as_view(), name='borrow-records-list'),
    path('borrow-records-details/<int:pk>/', BorrowRecordRetrieveUpdateView.as_view(), name='borrow-records-details')
]
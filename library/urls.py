from django.urls import path
from library.views import BookListCreateView, BookRetrieveUpdateDestroyView, BorrowRecordListCreateView, BorrowRecordRetrieveUpdateDestroyView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
    path('borrow/', BorrowRecordListCreateView.as_view(), name='borrow-record-list-create'),
    path('borrow/<int:pk>/', BorrowRecordRetrieveUpdateDestroyView.as_view(), name='borrow-record-retrieve-update-destroy'),
]
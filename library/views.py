from rest_framework import generics
from .models import Book, BorrowRecord
from .serializers import (
    BookListCreateSerializer, 
    BookDetailsSerializer, 
    BorrowRecordListCreateSerializer, 
    BorrowRecordDetailsSerializer
)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListCreateSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer

class BorrowRecordListCreateView(generics.ListCreateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordListCreateSerializer

class BorrowRecordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordDetailsSerializer
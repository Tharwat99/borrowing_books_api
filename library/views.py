from rest_framework import generics
from .models import Book, BorrowRecord
from .serializers import (
    BookListSerializer, 
    BookDetailsSerializer, 
    BorrowRecordCreateSerializer, 
    BorrowRecordListSerializer,
    BorrowRecordDetailsSerializer
)

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer

class BorrowRecordCreateView(generics.CreateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordCreateSerializer

class BorrowRecordListView(generics.ListAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordListSerializer

class BorrowRecordRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordDetailsSerializer
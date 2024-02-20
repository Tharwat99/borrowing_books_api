from rest_framework import generics, permissions
from .models import Book, BorrowRecord
from .permissions import IsBorrowerOrAdmin
from .serializers import (
    BookCreateSerializer,
    BookListSerializer, 
    BookDetailsSerializer, 
    BorrowRecordCreateSerializer, 
    BorrowRecordListSerializer,
    BorrowRecordDetailsSerializer
)

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [permissions.IsAdminUser]
    
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
    queryset = BorrowRecord.objects.select_related('book').select_related('borrower').all()
    serializer_class = BorrowRecordListSerializer
    permission_classes = [permissions.IsAdminUser]

class BorrowRecordRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordDetailsSerializer
    permission_classes = [IsBorrowerOrAdmin]
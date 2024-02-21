from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .models import Book, BorrowRecord
from .permissions import IsBorrowerOrAdmin
from .serializers import (
    BookCreateSerializer,
    BookListSerializer, 
    BookDetailsSerializer, 
    BorrowRecordCreateSerializer, 
    BorrowRecordListSerializer,
    BorrowRecordRetrieveSerializer,
    BorrowRecordUpdateSerializer
)
from .paginations import BorrowerRecordsListPagination
from .filters import BorrowRecordListFilter

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
    pagination_class = BorrowerRecordsListPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BorrowRecordListFilter

class BorrowRecordRetrieveView(generics.RetrieveAPIView):
    queryset = BorrowRecord.objects.select_related('book').select_related('borrower').all()
    serializer_class = BorrowRecordRetrieveSerializer
    permission_classes = [IsBorrowerOrAdmin]

class BorrowRecordUpdateView(generics.UpdateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordUpdateSerializer
    permission_classes = [IsBorrowerOrAdmin]
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
from .models import Book, BorrowRecord
from .permissions import IsBorrowerOrAdmin
from .serializers import (
    BookCreateSerializer,
    BookListSerializer, 
    BookRetrieveSerializer,
    BookUpdateSerializer, 
    BorrowRecordCreateSerializer, 
    BorrowRecordListSerializer,
    BorrowRecordRetrieveSerializer,
    BorrowRecordUpdateSerializer
)
from .paginations import BooksListPagination, BorrowerRecordsListPagination
from .filters import BookListFilter, BorrowRecordListFilter

@extend_schema(
    request={
        'application/json': {
            'type': 'object',
            'properties': {
                'title': {'type': 'string'},
                'author': {'type': 'string'},
                'is_avaliable': {'type': 'boolean'},
               
            }
        },
    },
    responses={
        200: BookCreateSerializer, 
        400: OpenApiResponse(response= 400, description="Bad Request",
            examples= [
                OpenApiExample(name="Example 1", description="Book title is required to create book",
                    value= {
                        "title": [
                            "This field may not be blank."
                        ]
                    }
                ),
                OpenApiExample(name="Example 2", description="Book author is required to create book",
                    value= { "author": [
                        "This field may not be blank."
                        ]
                    }
                ),
                OpenApiExample(name="Example 3", description="Title and author is required to create book",
                    value= { 
                        "title": [
                            "This field may not be blank."
                        ],
                        "author": [
                        "This field may not be blank."
                        ]
                    }
                ),
        ]),
        401: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Authentication credentials were not provided.'}}},        
        403: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'You do not have permission to perform this action.'}}},        
    
    },
    description= 
    """
    Endpoint to create book with title and author.
    """
)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [permissions.IsAdminUser]

@extend_schema( 
    responses={
        200: BookListSerializer, 
        401: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Authentication credentials were not provided.'}}},        
    
    },
    description= 
    """
    Endpoint to list all books.
    """
)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    pagination_class = BooksListPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BookListFilter

@extend_schema( 
    responses={
        200: BookRetrieveSerializer, 
        401: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Authentication credentials were not provided.'}}},        
    
    },
    description= 
    """
    Endpoint to retrieve book by id.
    """
)
class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookRetrieveSerializer

@extend_schema( 
    responses={
        200: BookUpdateSerializer, 
        400: OpenApiResponse(response= 400, description="Bad Request",
            examples= [
                OpenApiExample(name="Example 1", description="Book title is required to create book",
                    value= {
                        "title": [
                            "This field may not be blank."
                        ]
                    }
                ),
                OpenApiExample(name="Example 2", description="Book author is required to create book",
                    value= { "author": [
                        "This field may not be blank."
                        ]
                    }
                ),
                OpenApiExample(name="Example 3", description="Title and author is required to create book",
                    value= { 
                        "title": [
                            "This field may not be blank."
                        ],
                        "author": [
                        "This field may not be blank."
                        ]
                    }
                ),
        ]),
        401: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Authentication credentials were not provided.'}}},        
    
    },
    description= 
    """
    Endpoint to update book by id and new data.
    """
)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer
    permission_classes = [permissions.IsAdminUser]   

@extend_schema(
    request={
        'application/json': {
            'type': 'object',
            'properties': {
                'book': {'type': 'integer'},
                'borrower': {'type': 'integer'}
               
            }
        },
    },
    responses={
        200: BorrowRecordCreateSerializer, 
        400: OpenApiResponse(response= 400, description="Bad Request",
            examples= [
                OpenApiExample(name="Example 1", description="Book is not available to borrow at the moment",
                    value= {
                        "details": "Book is not available to borrow at the moment."
                    }
                ),
                OpenApiExample(name="Example 2", description="Book is required to create borrow record",
                    value= { "book": [
                        "Book is required."
                        ]
                    }
                ),
                OpenApiExample(name="Example 3", description="Borrower is required to create borrow record",
                    value= { "borrower": [
                        "Borrower is required."
                        ]
                    }
                ),
                
                OpenApiExample(name="Example 4", description="Title and author is required to create book",
                    value= { 
                        "book": [
                        "Book is required."
                        ],
                        "borrower": [
                        "Borrower is required."
                        ]
                    }
                ),
        ]),
        401: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Authentication credentials were not provided.'}}},        
        403: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'You do not have permission to perform this action.'}}},        
        404: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Not found'}}},        
    
    },
    description= 
    """
    Endpoint to create borrow book record with book and user borrower.
    """
)
class BorrowRecordCreateView(generics.CreateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordCreateSerializer

@extend_schema(
    responses={
        200: BorrowRecordListSerializer, 
        401: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Authentication credentials were not provided.'}}},        
        403: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'You do not have permission to perform this action.'}}},        
    },
    description= 
    """
    Endpoint to list all borrow book records.
    """
)
class BorrowRecordListView(generics.ListAPIView):
    queryset = BorrowRecord.objects.select_related('book').select_related('borrower').all()
    serializer_class = BorrowRecordListSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = BorrowerRecordsListPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BorrowRecordListFilter

@extend_schema(
    responses={
        200: BorrowRecordRetrieveSerializer, 
        401: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Authentication credentials were not provided. '}}},        
        403: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'You do not have permission to perform this action.'}}},        
        404: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Not found'}}},        
    
    },
    description= 
    """
    Endpoint to get borrow book record by id.
    """
)
class BorrowRecordRetrieveView(generics.RetrieveAPIView):
    queryset = BorrowRecord.objects.select_related('book').select_related('borrower').all()
    serializer_class = BorrowRecordRetrieveSerializer
    permission_classes = [IsBorrowerOrAdmin]

@extend_schema( 
    responses={
        200: BorrowRecordUpdateSerializer, 
        400: OpenApiResponse(response= 400, description="Bad Request",
            examples= [
                OpenApiExample(name="Example 1", description="Book is not available to borrow at the moment",
                    value= {
                        "details": "Book is not available to borrow at the moment."
                    }
                ),
                OpenApiExample(name="Example 2", description="Book is required to create borrow record",
                    value= { "book": [
                        "Book is required."
                        ]
                    }
                ),
                OpenApiExample(name="Example 3", description="Borrower is required to create borrow record",
                    value= { "borrower": [
                        "Borrower is required."
                        ]
                    }
                ),
                
                OpenApiExample(name="Example 4", description="Title and author is required to create book",
                    value= { 
                        "book": [
                        "Book is required."
                        ],
                        "borrower": [
                        "Borrower is required."
                        ]
                    }
                ),
        ]),
        401: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Authentication credentials were not provided. '}}},        
        403: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'You do not have permission to perform this action.'}}},        
        404: {'type': 'object', 'properties': {'detail': {'type': 'string', 'default':'Not found'}}},        
    
    },
    description= 
    """
    Endpoint to update borrow book record by id and new data.
    """
)
class BorrowRecordUpdateView(generics.UpdateAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordUpdateSerializer
    permission_classes = [IsBorrowerOrAdmin]
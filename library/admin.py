from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Book, BorrowRecord

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'is_available')
    list_editable = ('title', 'is_available')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('id','book', 'borrower', 'borrow_date', 'return_date')
    list_filter = ('book__title', 'borrower__username')
    search_fields = ('book__title', 'borrower__username')

    
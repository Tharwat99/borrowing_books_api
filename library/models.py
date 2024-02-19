from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = "books"
        verbose_name = _("book")
        verbose_name_plural = _("footers")
        ordering = ["title"]

    def __str__(self):
        return "%s" % (self.title)


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} ({self.borrower_name})"
    
    class Meta:
        db_table = "borrow_records"
        verbose_name = _("borrow record")
        verbose_name_plural = _("borrow records")
        ordering = ["-borrow_date"]

    def __str__(self):
        return "Book title: %s, Borrower name: %s, Borrow date: %s, return date: %s," % (self.title, self.borrower_name, self.borrow_date, self.return_date)
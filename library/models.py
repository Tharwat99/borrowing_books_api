from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from user.models import User
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_available = models.BooleanField(default = True)

    class Meta:
        db_table = "books"
        verbose_name = _("book")
        verbose_name_plural = _("books")
        ordering = ["title"]

    def __str__(self):
        return "%s" % (self.title)

    def check_availability(self, borrower=None):
        print(borrower)
        current_date = timezone.now().date()
        borrow_records = self.borrowrecord_set.filter(
        ~Q(borrower = borrower) &
        Q(Q(return_date__gt=current_date) | Q(return_date=None))
        ).order_by('return_date')
        print(borrow_records)
        print(borrow_records.exists())
        return not borrow_records.exists() 

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} ({self.borrower_name})"
    
    class Meta:
        db_table = "borrow_records"
        verbose_name = _("borrow record")
        verbose_name_plural = _("borrow records")
        ordering = ["-borrow_date"]

    def clean(self):
        super().clean()
        
        if not self.book_id:
            raise ValidationError("Book is required.")
        if not self.borrower_id:
            raise ValidationError("Book is required.")
        if not self.book.check_availability(self.borrower):
            raise ValidationError("Book is not available to borrow at the moment.")
        if self.id == None and not self.book.check_availability():
            raise ValidationError("Book is not available to borrow at the moment.")
        
        if self.return_date and self.return_date <= self.borrow_date:
            raise ValidationError("Return date should be after the borrow date.")
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Book title: %s, Borrower name: %s, Borrow date: %s, return date: %s," % (self.book.title, self.borrower.username, self.borrow_date, self.return_date)


@receiver(post_save, sender=BorrowRecord)
def update_book_availability(sender, instance, created, **kwargs):
    if created:
        # Book is being borrowed
        instance.book.is_available = False
        instance.book.save()
    elif instance.return_date != None and instance.return_date < timezone.now().date():
        # Book is being returned
        instance.book.is_available = True
        instance.book.save()

@receiver(post_delete, sender=BorrowRecord)
def update_book_availability(sender, instance, **kwargs):
        instance.book.is_available= instance.book.check_availability()    
        instance.book.save()
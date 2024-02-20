from django.contrib import admin
from .models import User

@admin.register(User)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name')
    list_editable = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
    search_fields = ('username', 'email')
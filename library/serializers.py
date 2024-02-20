from rest_framework import serializers
from .models import Book, BorrowRecord
from user.serializers import UserSerializer

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowRecordCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BorrowRecord
        fields = ('book', 'borrower')
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except Exception as e:
            raise serializers.ValidationError({"details": e.args[0]})
        
    

class BorrowRecordListSerializer(serializers.ModelSerializer):
    book = BookDetailsSerializer()
    borrower = UserSerializer()

    class Meta:
        model = BorrowRecord
        fields = '__all__'
    def validate(self, attrs):
        try:
            super().validate(attrs)
        except Exception as e:
            print(e)
        
class BorrowRecordDetailsSerializer(serializers.ModelSerializer):
    book = BookDetailsSerializer()
    borrower = UserSerializer()

    class Meta:
        model = BorrowRecord
        fields = '__all__'
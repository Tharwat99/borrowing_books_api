from rest_framework import serializers
from .models import Book, BorrowRecord
from user.serializers import UserSerializer

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'

class BookRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookUpdateSerializer(serializers.ModelSerializer):
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
    book = BookRetrieveSerializer()
    borrower = UserSerializer()

    class Meta:
        model = BorrowRecord
        fields = '__all__'
        
class BorrowRecordRetrieveSerializer(serializers.ModelSerializer):
    book = BookRetrieveSerializer()
    borrower = UserSerializer()

    class Meta:
        model = BorrowRecord
        fields = '__all__'

class BorrowRecordUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BorrowRecord
        fields = '__all__'
    
    def update(self, instance, validated_data):
        try:
            return super().update(instance, validated_data)
        except Exception as e:
            print("hello here")
            raise serializers.ValidationError({"details": e.args[0]})
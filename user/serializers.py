from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=128, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'id':{'read_only':True},
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)   
        return user
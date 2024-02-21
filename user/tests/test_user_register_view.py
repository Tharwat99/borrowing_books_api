import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from ..models import User
    
@pytest.mark.django_db
class TestUserRegisterView:
    register_url = reverse('register')
    
    def test_register_user_success(self, api_client):
        data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            "password":"testpassword"
        }
        response = api_client.post(self.register_url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username=data['username']).exists()
    
    def test_register_username_exists(self, api_client, user_factory):
        user1 = user_factory()
        
        data = {
            'username': user1.username,
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@test.com',
            "password":"testpassword"
        }
        response = api_client.post(self.register_url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert User.objects.filter(username=data['username']).count() > 0
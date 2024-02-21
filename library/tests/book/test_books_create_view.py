import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from ...models import Book
    
@pytest.mark.django_db
class TestBookCreateView:
    book_create_url = reverse('book-create')
    
    def test_book_creation_success(self, create_admin_user_token, api_client):
        data = {
            'title': 'test book',
            'author': 'test author'
        }
        token_data = create_admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.post(self.book_create_url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Book.objects.filter(title=data['title']).exists()
    
    def test_book_creation_forbidden(self, create_normal_user_token, api_client):
        data = {
            'title': 'test book',
            'author': 'test author'
        }
        token_data = create_normal_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.post(self.book_create_url, data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert not Book.objects.filter(title=data['title']).exists()
    
    def test_book_creation_unauthorized(self, api_client):
        data = {
            'title': 'test book',
            'author': 'test author'
        }
        response = api_client.post(self.book_create_url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert not Book.objects.filter(title=data['title']).exists()
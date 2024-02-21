import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from ...models import Book

@pytest.mark.django_db
class TestBookListView:
    book_list_url = reverse('book-list')
    
    def test_book_list_admin_success(self, create_admin_user_token, api_client, book_factory):
        book1 = book_factory()
        book2 = book_factory()
        book3 = book_factory()
        token_data = create_admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.get(self.book_list_url)
        assert response.status_code == status.HTTP_200_OK
        assert Book.objects.count() == 3
    
    def test_book_list_normal_success(self, create_normal_user_token, api_client, book_factory):
        book1 = book_factory()
        book2 = book_factory()
        book3 = book_factory()
        token_data = create_normal_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.get(self.book_list_url)
        assert response.status_code == status.HTTP_200_OK
        assert Book.objects.count() == 3
    
    def test_book_list_unauthorized(self, api_client, book_factory):
        book1 = book_factory()
        book2 = book_factory()
        book3 = book_factory()
        response = api_client.get(self.book_list_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    
    
   
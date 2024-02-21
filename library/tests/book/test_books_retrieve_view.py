import pytest
from rest_framework import status
from rest_framework.reverse import reverse

@pytest.mark.django_db
class TestBookRetrieveView:
    
    def test_book_retrieve_admin_success(self, create_admin_user_token, api_client, book_factory):
        book1 = book_factory()
        token_data = create_admin_user_token
        retrieve_url = reverse('book-retrieve', kwargs={'pk': book1.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.get(retrieve_url)
        assert response.status_code == status.HTTP_200_OK
        
    def test_book_retrieve_normal_success(self, create_normal_user_token, api_client, book_factory):
        book1 = book_factory()
        token_data = create_normal_user_token
        retrieve_url = reverse('book-retrieve', kwargs={'pk': book1.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.get(retrieve_url)
        assert response.status_code == status.HTTP_200_OK
        
        
    def test_book_retrieve_unauthorized(self, api_client, book_factory):
        book1 = book_factory()
       
        retrieve_url = reverse('book-retrieve', kwargs={'pk': book1.id})
        response = api_client.get(retrieve_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        book1.refresh_from_db()
        assert book1.title == "title11"
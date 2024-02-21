import pytest
from rest_framework import status
from rest_framework.reverse import reverse

@pytest.mark.django_db
class TestBookUpdateView:
    
    def test_book_update_admin_success(self, create_admin_user_token, api_client, book_factory):
        book1 = book_factory()
        token_data = create_admin_user_token
        assert book1.title == "title12"
        new_data = {
            "title": "newtitle"
        }
        # Build the URL with the book ID
        update_url = reverse('book-update', kwargs={'pk': book1.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        # Make the update request with the new data
        response = api_client.patch(update_url, data=new_data)
        assert response.status_code == status.HTTP_200_OK
        # Refresh the book instance from the database
        book1.refresh_from_db()
        assert book1.title == "newtitle"

    def test_book_update_forbidden(self, create_normal_user_token, api_client, book_factory):
        book1 = book_factory()
        token_data = create_normal_user_token
        assert book1.title == "title13"
        new_data = {
            "title": "newtitle"
        }
        # Build the URL with the book ID
        update_url = reverse('book-update', kwargs={'pk': book1.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        # Make the update request with the new data
        response = api_client.patch(update_url, data=new_data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        # Refresh the book instance from the database
        book1.refresh_from_db()
        assert book1.title == "title13"
    
    def test_book_update_unauthorized(self, api_client, book_factory):
        book1 = book_factory()
        assert book1.title == "title14"
        new_data = {
            "title": "newtitle"
        }
        # Build the URL with the book ID
        update_url = reverse('book-update', kwargs={'pk': book1.id})
        # Make the update request with the new data
        response = api_client.patch(update_url, data=new_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        # Refresh the book instance from the database
        book1.refresh_from_db()
        assert book1.title == "title14"
import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils import timezone

@pytest.mark.django_db
class TestBorrowRecordsRetrieveView:
    
    def test_borrow_record_retrieve_admin_success(self, create_admin_user_token, api_client, book_factory, user_factory, borrow_factory):
        book = book_factory()
        user = user_factory()
        borrower_record = borrow_factory(book=book, borrower=user)
        token_data = create_admin_user_token
        retrieve_url = reverse('borrow-records-retrieve', kwargs={'pk': borrower_record.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.get(retrieve_url)
        assert response.status_code == status.HTTP_200_OK
    
    def test_borrow_record_retrieve_normal_success(self, create_normal_user_token, api_client, book_factory, borrow_factory):
        book = book_factory()
        token_data = create_normal_user_token
        borrower_record = borrow_factory(book=book, borrower=token_data['user'])
        retrieve_url = reverse('borrow-records-retrieve', kwargs={'pk': borrower_record.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.get(retrieve_url)
        assert response.status_code == status.HTTP_200_OK
       
    
    def test_borrow_record_retrieve_forbidden(self, create_normal_user_token, api_client, book_factory, user_factory, borrow_factory):
        book = book_factory()
        user = user_factory()
        token_data = create_normal_user_token
        borrower_record = borrow_factory(book=book, borrower=user)
        retrieve_url = reverse('borrow-records-retrieve', kwargs={'pk': borrower_record.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.get(retrieve_url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_borrow_record_retrieve_unauthorized(self, api_client, book_factory, user_factory, borrow_factory):
        book = book_factory()
        user = user_factory()
        borrower_record = borrow_factory(book=book, borrower=user)
       
        retrieve_url = reverse('borrow-records-retrieve', kwargs={'pk': borrower_record.id})
        response = api_client.get(retrieve_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils import timezone

@pytest.mark.django_db
class TestBorrowRecordsUpdateView:
    
    def test_borrow_record_update_admin_success(self, create_admin_user_token, api_client, book_factory, user_factory, borrow_factory):
        book = book_factory()
        user = user_factory()
        borrower_record = borrow_factory(book=book, borrower=user)
        token_data = create_admin_user_token
        date_now = timezone.now().date()
        
        new_data = {
            "return_date": date_now
        }
        update_url = reverse('borrow-records-update', kwargs={'pk': borrower_record.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        # Make the update request with the new data
        response = api_client.patch(update_url, data=new_data)
        assert response.status_code == status.HTTP_200_OK
        borrower_record.refresh_from_db()
        assert borrower_record.return_date == date_now
    
    def test_borrow_record_update_normal_success(self, create_normal_user_token, api_client, book_factory, borrow_factory):
        book = book_factory()
        token_data = create_normal_user_token
        borrower_record = borrow_factory(book=book, borrower=token_data['user'])
        date_now = timezone.now().date()
        new_data = {
            "return_date": date_now
        }
        update_url = reverse('borrow-records-update', kwargs={'pk': borrower_record.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        # Make the update request with the new data
        response = api_client.patch(update_url, data=new_data)
        assert response.status_code == status.HTTP_200_OK
        borrower_record.refresh_from_db()
        assert borrower_record.return_date == date_now
    
    def test_borrow_record_update_forbidden(self, create_normal_user_token, api_client, book_factory, user_factory, borrow_factory):
        book = book_factory()
        user = user_factory()
        token_data = create_normal_user_token
        date_now = timezone.now().date()
        borrower_record = borrow_factory(book=book, borrower=user)
        new_data = {
            "return_date": date_now
        }
        update_url = reverse('borrow-records-update', kwargs={'pk': borrower_record.id})
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        # Make the update request with the new data
        response = api_client.patch(update_url, data=new_data)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        borrower_record.refresh_from_db()
        assert borrower_record.return_date == None

    def test_borrow_record_update_unauthorized(self, api_client, book_factory, user_factory, borrow_factory):
        book = book_factory()
        user = user_factory()
        date_now = timezone.now().date()
        borrower_record = borrow_factory(book=book, borrower=user)
        new_data = {
            "return_date": date_now
        }
        update_url = reverse('borrow-records-update', kwargs={'pk': borrower_record.id})
        # Make the update request with the new data
        response = api_client.patch(update_url, data=new_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        borrower_record.refresh_from_db()
        assert borrower_record.return_date == None

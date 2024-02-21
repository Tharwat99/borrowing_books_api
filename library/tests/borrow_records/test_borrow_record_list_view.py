import pytest
from rest_framework import status
from rest_framework.reverse import reverse

@pytest.mark.django_db
class TestBorrowRecordsListView:
    borrow_records_list_url = reverse('borrow-records-list')
    
    def test_borrow_record_list_admin_success(self, create_admin_user_token, api_client, book_factory, user_factory, borrow_factory):
        user1 = user_factory()
        user2 = user_factory()
        book1 = book_factory()
        book2 = book_factory()
        borrow_factory1 = borrow_factory(book = book1, borrower = user1)
        borrow_factory2 = borrow_factory(book = book2, borrower = user2)
        token_data = create_admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.get(self.borrow_records_list_url)
        assert response.status_code == status.HTTP_200_OK
    
    def test_borrow_record_list_forbidden(self, create_normal_user_token, api_client):
        token_data = create_normal_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.get(self.borrow_records_list_url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
    
    def test_borrow_record_list_unauthorized(self, api_client):
        response = api_client.get(self.borrow_records_list_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    
    
   
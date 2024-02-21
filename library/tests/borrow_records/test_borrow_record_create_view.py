import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from ...models import BorrowRecord
    
@pytest.mark.django_db
class TestBorrowRecordsCreateView:
    borrow_records_create_url = reverse('borrow-records-create')
    
    def test_borrow_record_creation_admin_success(self, create_admin_user_token, api_client, book_factory, user_factory):
        book = book_factory()
        user = user_factory()
        data = {
            'book':book.id,
            'borrower':user.id
        }
        token_data = create_admin_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.post(self.borrow_records_create_url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert BorrowRecord.objects.filter(book=data['book']).exists()
    
    def test_borrow_record_creation_normal_success(self, create_normal_user_token, api_client, book_factory, user_factory):
        book = book_factory()
        user = user_factory()
        data = {
            'book':book.id,
            'borrower':user.id
        }
        token_data = create_normal_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.post(self.borrow_records_create_url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert BorrowRecord.objects.filter(book=data['book']).exists()

    def test_borrow_record_creation_unauthorized(self, api_client, book_factory, user_factory):
        
        book = book_factory()
        user = user_factory()
        data = {
            'book':book.id,
            'borrower':user.id
        }
        response = api_client.post(self.borrow_records_create_url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert not BorrowRecord.objects.filter(book=data['book']).exists()
    
    def test_borrow_record_creation_book_required(self, api_client, create_normal_user_token, user_factory):
        
        user = user_factory()
        data = {
            'borrower':user.id
        }

        token_data = create_normal_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.post(self.borrow_records_create_url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'book' in response.json()
        assert response.json()['book'][0] == "This field is required."
        assert not BorrowRecord.objects.filter(borrower=data['borrower']).exists()
    
    def test_borrow_record_creation_borrower_required(self, api_client, create_normal_user_token, book_factory):
        
        book = book_factory()
        data = {
            'book':book.id
        }

        token_data = create_normal_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.post(self.borrow_records_create_url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'borrower' in response.json()
        assert response.json()['borrower'][0] == "This field is required."
        assert not BorrowRecord.objects.filter(book=data['book']).exists()
    
    def test_borrow_record_creation_not_avaliable(self, api_client, create_normal_user_token, book_factory, user_factory, borrow_factory):
        
        book = book_factory()
        user1 = user_factory()
        user2 = user_factory()
        borrow_record = borrow_factory(book=book, borrower=user1)
        data = {
            'book':book.id,
            'borrower':user2.id
        }

        token_data = create_normal_user_token
        api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data['access'])
        response = api_client.post(self.borrow_records_create_url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['details'] == 'Book is not available to borrow at the moment.'
        assert not BorrowRecord.objects.filter(borrower=data['borrower']).exists()
    
    

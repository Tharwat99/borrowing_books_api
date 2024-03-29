import pytest
from rest_framework import status
from rest_framework.reverse import reverse

@pytest.mark.django_db
class TestUserTokenView:
    token_obtain_pair_url = reverse('token-obtain-pair')
    token_refresh_token_url = reverse('token-refresh')
    
    def test_token_obtain_pair_success(self, api_client, user_factory):
        user1 = user_factory()
        
        data = {
            "username": user1.username,
            "password": "testpassword"
        }
        response = api_client.post(self.token_obtain_pair_url, data)
        assert response.status_code == status.HTTP_200_OK

    def test_token_obtain_pair_failure(self, api_client, user_factory):
        user1 = user_factory()
        
        data = {
            "username": user1.username,
            "password": "wrongpassword"
        }
        response = api_client.post(self.token_obtain_pair_url, data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_token_refresh_token(self, api_client, user_factory):
        user1 = user_factory()
        data = {
            "username": user1.username,
            "password":"testpassword"
        }

        response = api_client.post(self.token_obtain_pair_url, data)
        assert response.status_code == status.HTTP_200_OK
        
        data = {
            "refresh": response.data['refresh'],
        }
        response = api_client.post(self.token_refresh_token_url, data)
        assert response.status_code == status.HTTP_200_OK
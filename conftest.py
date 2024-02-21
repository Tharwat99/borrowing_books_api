import pytest
from pytest_factoryboy import register
from user.tests.factories import UserFactory
from library.tests.factories import BookFactory, BorrowFactory
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

register(UserFactory) 
register(BookFactory) 
register(BorrowFactory) 

@pytest.fixture
def api_client():
   return APIClient()

@pytest.fixture
def create_normal_user_token(db, user_factory):
   user = user_factory()
   refresh = RefreshToken.for_user(user)
   return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
   }

@pytest.fixture
def create_admin_user_token(db, user_factory):
   user = user_factory(is_superuser=True, is_staff=True)
   refresh = RefreshToken.for_user(user)
   return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
   }
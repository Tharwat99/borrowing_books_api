import pytest
from pytest_factoryboy import register
from user.tests.factories import UserFactory
from rest_framework.test import APIClient

register(UserFactory) 

@pytest.fixture
def api_client():
   return APIClient()
import pytest

@pytest.fixture(scope='class')
@pytest.mark.django_db  
def test_user_factory(user_factory):
   user = user_factory()
   assert user.username == 'username0'

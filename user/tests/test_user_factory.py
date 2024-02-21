import pytest

@pytest.mark.django_db
def test_user_user_factory(user_factory):
   user = user_factory()
   assert user.username == 'username0'

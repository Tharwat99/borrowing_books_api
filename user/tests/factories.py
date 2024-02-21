import factory
from ..models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
       model = User

    username = factory.Sequence(lambda n: f'username{n}')
    first_name = factory.Sequence(lambda n: f'first_name{n}')
    last_name = factory.Sequence(lambda n: f'last_name{n}')
    email = factory.Sequence(lambda n: f'test{n}@test.com')
    password = factory.PostGenerationMethodCall(
        'set_password', 'testpassword'
    )

from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    """
    User Base Model that extends AbstractUser and PermissionsMixin.
    """
    
    objects = UserManager()
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    
    class Meta:
        db_table = "users"

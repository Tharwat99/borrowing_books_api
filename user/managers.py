from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """
    user model manager.
    """
    def create_user(self, username, first_name, last_name, email, password = None, **extra_fields):
        """
        Create and save a user in db.
        """
        user = self.model(username=username, first_name = first_name,
        last_name = last_name, email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        """
        Create and save a user as super user in db.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(username, first_name, last_name, email, password, **extra_fields)
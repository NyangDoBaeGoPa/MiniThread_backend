from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, account_id, user_name, password=None, **extra_fields):
        user = self.model(account_id=account_id,
                          user_name=user_name, **extra_fields)
        user.set_password(password)

        return user

    def create_superuser(self, account_id, user_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(account_id, user_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    account_id = models.CharField(
        max_length=30,
        unique=True
    )
    user_name = models.CharField(
        max_length=30,
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )

    USERNAME_FIELD = 'account_id'
    REQUIRED_FIELDS = ['user_name']

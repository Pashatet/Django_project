from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid
from django.db.models import signals
from django.core.mail import send_mail
from django.urls import reverse


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email,
            password=password, **extra_fields

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    is_verified = models.BooleanField('verified', default=False)  # new
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)  # new

    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Есть ли у пользователей конкретное разрешение?"
        return True

    def has_module_perms(self, app_label):
        "Есть ли у пользователя разрешения на просмотр приложения `app_label`?"
        return True

    @property
    def is_staff(self):
        "Явнается ли пользователь сотрудником?"
        # Самый простой ответ: Все администраторы - это сотрудники
        return self.is_admin


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        send_mail(
            'Verify your  account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(instance.verification_uuid)}),
            'admin@localhost.ru',
            [instance.email],
            fail_silently=False,
        )


signals.post_save.connect(user_post_save, sender=User)

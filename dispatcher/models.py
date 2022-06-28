from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
			email=self.normalize_email(email),
			username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

class Act(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    act_type = models.CharField(max_length=20)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/act_images')

    class ActProcesses(models.TextChoices):
        waiting = 'Ожидание принятия заявки'
        accepted = 'Заявки принята'
        returned = 'Заявка возвращена'

    act_processing = models.CharField(max_length=25, choices=ActProcesses.choices, default=ActProcesses.waiting)
    do_until = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

# В каждом меню будет дополнительные подменю. Например:
# Заявки – В работе – Не выполненные – Просроченные – В обработке

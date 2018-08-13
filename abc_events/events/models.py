from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
            email = self.normalize_email(email)
            user = self.model(email = email, **extra_fields)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    # I had add the username field despite that I don't use in my User model
    username = models.CharField(('username'), max_length=30, null=True,
                                help_text=('Required. 30 characters or fewer. Letters, digits and ''@/./+/-/_ only.'),
                                validators=[RegexValidator(r'^[\w.@+-]+$', ('Enter a valid username.'), 'invalid')
                                            ])

    email = models.EmailField(unique=True, null=True,
                              help_text=('Required. Letters, digits and ''@/./+/-/_ only.'),
                              validators=[RegexValidator(r'^[\w.@+-]+$', ('Enter a valid email address.'), 'invalid')
                                          ])

    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this site.'),
    )

    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()
    USERNAME_FIELD = "email"

    class Meta:
        db_table = 'auth_user'
        verbose_name_plural = 'Usuarios en la plataforma'

    def __str__(self):
        return self.email


CATEGORY_CHOICES = (
    ('conferencia', 'CONFERENCIA'),
    ('seminario', 'SEMINARIO'),
    ('congreso', 'CONGRESO'),
    ('curso', 'CURSO'),

)

TYPE_EVENT_CHOICES = (
    ('presencial', 'PRESENCIAL'),
    ('virtual', 'VIRTUAL')

)


class Event(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='events', on_delete= models.CASCADE)
    name = models.CharField(max_length=250, null=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='conferencia')
    place = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    start_date = models.DateTimeField(default=timezone.now, editable=True)
    end_date = models.DateTimeField(default=timezone.now, editable=True)
    type_event = models.CharField(max_length=20, choices=TYPE_EVENT_CHOICES, default='presencial')


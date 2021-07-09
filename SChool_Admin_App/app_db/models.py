from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from datetime import datetime as dt


"""
Application models.

[x] User
[x] User_Profile
[x] Student
[] Course
[] Exam
[] ExamRetake



"""

"""
 
 ██╗   ██╗███████╗███████╗██████╗     ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗     
 ██║   ██║██╔════╝██╔════╝██╔══██╗    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║     
 ██║   ██║███████╗█████╗  ██████╔╝    ██╔████╔██║██║   ██║██║  ██║█████╗  ██║     
 ██║   ██║╚════██║██╔══╝  ██╔══██╗    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ██║     
 ╚██████╔╝███████║███████╗██║  ██║    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗
  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝
                                                                                  
 
"""


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def get_email_name(self):
        return(self.email.split('@')[0])


class User_Profile(models.Model):
    teacher = 1
    tutor = 2
    administration = 3
    maintenance = 4

    USER_ROLE_CHOICES = (
        (teacher, 'Maestro/a'),
        (tutor, 'Tutor'),
        (administration, 'Administracion'),
        (maintenance, 'Mantenimiento'),
    )
    sex_undefined = 0
    sex_man = 1
    sex_woman = 2
    SEX_CHOICES = (
        (sex_undefined, 'NO DEFINIDO'),
        (sex_man, 'Hombre'),
        (sex_woman, 'Mujer'),
    )
    profile_user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True)
    rol = models.IntegerField('Rol', choices=USER_ROLE_CHOICES, default=tutor)
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    age = models.IntegerField('Edad')
    sex = models.IntegerField(
        'Sexo', choices=SEX_CHOICES, default=sex_undefined)
    date_of_birth = models.DateField(
        'Fecha de Nacimiento', auto_now=False, auto_now_add=False)
    occupation = models.CharField('Ocupacion', max_length=50)


"""
 
  █████╗ ██████╗ ██████╗     ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗     ███████╗
 ██╔══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║     ██╔════╝
 ███████║██████╔╝██████╔╝    ██╔████╔██║██║   ██║██║  ██║█████╗  ██║     ███████╗
 ██╔══██║██╔═══╝ ██╔═══╝     ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ██║     ╚════██║
 ██║  ██║██║     ██║         ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗███████║
 ╚═╝  ╚═╝╚═╝     ╚═╝         ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
                                                                                 
 
"""


class Student(models.Model):

    name = models.CharField('Nombre', max_length=50)
    surname = models.CharField('Apellido', max_length=50)
    direction = models.CharField('Direccion', max_length=50)
    age = models.IntegerField('Edad')
    date_of_birth = models.DateField(
        'Fecha de Nacimiento', auto_now=False, auto_now_add=False)

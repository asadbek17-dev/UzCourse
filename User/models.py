from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models

class CustomUserManager(BaseUserManager):

    def create_user(self,username, email,first_name,last_name,password,is_ban, role):

        user = self.model(
            username,
            email,
            first_name,
            last_name,
            is_ban,
            role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    ROLES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student')
    )
    username = models.CharField(max_length=150,null=False,blank=False,unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, null=False,blank=False)
    last_name = models.CharField(max_length=150, null=False,blank=False)
    role = models.CharField(max_length=10, choices=ROLES, default='student')
    is_ban = models.BooleanField(default=False)
    joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyManager(BaseUserManager):

    def create_user(self, email, username, password = None):

        if not email:
            raise ValueError('Email required!')
        
        user = self.model(
            email = self.normalize_email(email=email),
            username = username,
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password):

        user = self.create_user(
            email,
            username = username,
            password = password,
        )

        user.is_admin = True
        user.save()
        return user
    

class MyUser(AbstractBaseUser):

    username = models.CharField("Username", max_length=50, unique=True)
    email = models.EmailField("Email", max_length=100, unique=True)
    name = models.CharField("Name", max_length=150, null=True, blank=True)
    img_perfil = models.ImageField("Perfil Image", upload_to='media', null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.username}"
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    

from django.db import models
from django.forms.widgets import PasswordInput

# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    # username = models.CharField(max_length=50, null=False, unique=True)
    email = models.EmailField(max_length=254, null=False, unique=True)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

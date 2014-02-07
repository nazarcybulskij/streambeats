from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser):
    
    email = models.EmailField(max_length=80, verbose_name=_('email'))
    first_name = models.EmailField()

    def __unicode__(self):
        return self.username

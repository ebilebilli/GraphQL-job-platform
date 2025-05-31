from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    is_employer = models.BooleanField(default=False)
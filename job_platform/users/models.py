from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.validators import LinkValidator

class CustomerUser(AbstractUser):
    MAN = 'Man'
    WOMAN = 'Woman'
    GENDER_CHOOSE_LIST = [
        (MAN, 'Man'),
        (WOMAN, 'Woman')
    ]

    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True)
    birthday = models.DateField()
    gender =  models.CharField(choices=GENDER_CHOOSE_LIST, max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    twitter_link = models.URLField(null=True, blank=True, validators=[LinkValidator.validate_twitter_link])
    linkedln_link = models.URLField(null=True, blank=True, validators=[LinkValidator.validate_linkedln_link])
    facebook_link = models.URLField(null=True, blank=True, validators=[LinkValidator.validate_facebook_link])
    youtube_link = models.URLField(null=True, blank=True, validators=[LinkValidator.validate_youtube_link])
    
    def __str__(self):
        return self.full_name
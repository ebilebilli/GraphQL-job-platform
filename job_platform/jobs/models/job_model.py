from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomerUser


User = get_user_model()


class Job(models.Model):
    EMPLOYMENT_FULL_TIME = 'FT'
    EMPLOYMENT_PART_TIME = 'PT'
    EMPLOYMENT_CONTRACT = 'CT'
    EMPLOYMENT_INTERNSHIP = 'IN'
    EMPLOYMENT_TEMPORARY = 'TP'

    EMPLOYMENT_TYPE_CHOICES = [
        (EMPLOYMENT_FULL_TIME, 'Full-time'),
        (EMPLOYMENT_PART_TIME, 'Part-time'),
        (EMPLOYMENT_CONTRACT, 'Contract'),
        (EMPLOYMENT_INTERNSHIP, 'Internship'),
        (EMPLOYMENT_TEMPORARY, 'Temporary'),
    ]

    employer = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='jobs',
    )
    
    company = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=55)
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE_CHOICES)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title} at {self.company}'
        
from django.contrib import admin
from .models.job_model import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'employer',
        'location',
        'employment_type',
        'salary_min',
        'salary_max',
        'is_active',
        'created_at',
    )
    list_filter = (
        'employment_type',
        'is_active',
        'created_at',
        'location',
    )
    search_fields = (
        'title',
        'company',
        'location',
        'description',
        'employer__username',
    )
    ordering = ('-created_at',)

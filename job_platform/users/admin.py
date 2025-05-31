from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomerUser


@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    model = CustomerUser
    list_display = ('username', 'full_name', 'email', 'phone_number', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'gender')
    search_fields = ('username', 'full_name', 'email', 'phone_number')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'email', 'phone_number', 'birthday', 'gender')}),
        ('Social Links', {'fields': ('twitter_link', 'linkedln_link', 'facebook_link', 'youtube_link')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'full_name', 'email', 'phone_number', 'birthday', 'gender', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
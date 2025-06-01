from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, RegexValidator
from datetime import datetime, timedelta, timezone


class LinkValidator:
    @staticmethod
    def validate_twitter_link(value):
        url_validator = URLValidator()
        try:
            url_validator(value)
            if value and not value.startswith("https://twitter.com/"):
                raise ValidationError("Twitter link must start with 'https://twitter.com/'.")
        except ValidationError:
            raise ValidationError("Enter a valid Twitter URL.")
        
    @staticmethod
    def validate_linkedln_link(value):
        url_validator = URLValidator()
        try:
            url_validator(value)
            if value and not value.startswith("https://www.linkedin.com/"):
                raise ValidationError("LinkedIn link must start with 'https://www.linkedin.com/'.")
        except ValidationError:
            raise ValidationError("Enter a valid LinkedIn URL.")

    @staticmethod
    def validate_facebook_link(value):
        url_validator = URLValidator()
        try:
            url_validator(value)
            if value and not value.startswith("https://www.facebook.com/"):
                raise ValidationError("Facebook link must start with 'https://www.facebook.com/'.")
        except ValidationError:
            raise ValidationError("Enter a valid Facebook URL.")

    @staticmethod
    def validate_youtube_link(value):
        url_validator = URLValidator()
        try:
            url_validator(value)
            if value and not value.startswith("https://www.youtube.com/"):
                raise ValidationError("YouTube link must start with 'https://www.youtube.com/'.")
        except ValidationError:
            raise ValidationError("Enter a valid YouTube URL.")


def validate_birthday(value):
    today = timezone.now().date()
    min_allowed_date = today - timedelta(days=365*100)
    min_allowed_age = today - timedelta(days=365 * 13)
    
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, '%d-%m-%Y').date()
        except ValueError:
            raise ValidationError("Date format is incorrect. It should be: DD-MM-YYYY")
    
    if value > today:
        raise ValidationError("Birthday cannot be a future date.")
    
    if value > min_allowed_age:
        raise ValidationError("User must be at least 13 years old.")
    
    if value < min_allowed_date:
        raise ValidationError("Birthday cannot be more than 100 years ago.")


phone_validator = RegexValidator(
    regex=r'^(50|51|55|70|77|99)[0-9]{7}$',
    message="Phone number is not valid. Enter it in the format: 50 123 45 67."
)
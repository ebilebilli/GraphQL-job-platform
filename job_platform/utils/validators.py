from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


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
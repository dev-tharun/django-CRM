import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_custom_email(value):
    # Regular expression to match the required pattern
    pattern = r'^(?=.*[a-z])(?=.*\d).+$'

    if not re.match(pattern, value):
        raise ValidationError(
            _('Please enter a valid email.'),
            params={'value': value},
        )

def validate_mobile_number(value):
    pattern = r'^[6-9]\d{9}$'
    if not re.match(pattern, value):
        raise ValidationError(
            _('Please enter a valid mobile number.'),
            params={'value': value},
        )

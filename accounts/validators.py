from django.core.validators import MinValueValidator
import re
from django.core.exceptions import ValidationError

min_weight_validator = MinValueValidator(30, message="Weight must be at least 30 kg.")
min_height_validator = MinValueValidator(130, message="Height must be at least 130 cm.")

def validate_username(value):
    username_regex = r'^[a-zA-Z0-9]+$'
    if not re.match(username_regex, value):
        raise ValidationError("Username must contain only letters and digits.")




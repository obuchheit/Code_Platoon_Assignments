from django.core.exceptions import ValidationError
import re

def validate_pokemon_name(name):
    error_message = "Improper name Format"

    regex = r'^[A-Z][a-z]*$'

    good_name = re.match(regex, name)

    if good_name:
        return name 
    else:
        raise ValidationError(error_message, params={'name': name})
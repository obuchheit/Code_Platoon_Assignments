from django.db import models
from django.utils import timezone
from django.core import validators as v
from .validators import validate_pokemon_name

class Pokemon(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, validators=[validate_pokemon_name])
    level = models.IntegerField(default=1, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])
    date_encountered = models.DateField(default="2015-01-01")
    date_captured = models.DateTimeField(default=timezone.now)
    description = models.TextField(default="Unknown", validators=[v.MinLengthValidator(6), v.MaxLengthValidator(150)])
    captured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} {"Has been caught" if self.captured else "Has not been cought"}"
    
    def level_up(self):
        self.level += 1
        self.full_clean() #prevents any attributes to be saved in the DB that don't pass the validators. Shell will still show the update though.
        self.save()

    def change_caught_status(self):
        self.captured = not self.captured
        self.save()
        
    
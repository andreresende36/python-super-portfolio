from django.db import models
from django.core.validators import URLValidator, MaxLengthValidator


class Profile(models.Model):
    name = models.CharField(
        max_length=100, validators=[MaxLengthValidator(limit_value=50)]
    )
    github = models.URLField(validators=[URLValidator()])
    linkedin = models.URLField(validators=[URLValidator()])
    bio = models.TextField(validators=[MaxLengthValidator(limit_value=500)])

    def __str__(self):
        return self.name

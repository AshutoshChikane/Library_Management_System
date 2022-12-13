from django.db import models
from django.forms import ValidationError

# Create your models here.


class Book(models.Model):
    Book = models.CharField(max_length=100)
    Author = models.CharField(max_length=50)
    Quantity = models.IntegerField(default=1)
    alotment = models.IntegerField(default=0)

    def clean(self):
        if self.alotment > self.Quantity:
            raise ValidationError(
                "alotted books cannot be greater than total books")

    @property
    def combined(self):
        return self.Quantity - self.alotment

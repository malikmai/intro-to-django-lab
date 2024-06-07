from django.db import models

# Create your models here.

class Location(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"
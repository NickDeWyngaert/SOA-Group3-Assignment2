from django.db import models

# Create your models here.

class To_do_item(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    deadline = models.DateField()
    soort = models.CharField(max_length=50)

    def __str__(self):
        return self.name

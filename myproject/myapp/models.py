from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=255),
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.name
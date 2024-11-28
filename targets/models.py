from django.db import models

class Target(models.Model):
    identifier = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    expiration_date = models.DateField()

    def __str__(self):
        return self.name
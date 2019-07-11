from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Countries(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    speakers = models.PositiveIntegerField()
    family = models.ManyToManyField(Family)
    countries = models.ManyToManyField(Countries)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0)
    manufacturer = models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return str(self.title) + ' ' + str(self.manufacturer)

    class Meta:
        abstract = True


class TV(Article):
    model = models.CharField(max_length=100)
    screen_size=models.CharField(max_length=100)
    power_consumption=models.PositiveIntegerField(default=0)


class Chair(Article):
    type = models.CharField(max_length=100)
    weight = models.FloatField(default=0)

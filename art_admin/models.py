from django.db import models

# Create your models here.

class Article(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    size = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    offer = models.BooleanField(default=False)

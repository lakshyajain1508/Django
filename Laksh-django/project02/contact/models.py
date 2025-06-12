from django.db import models
class Msg(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile= models.BigIntegerField()
    msg = models.TextField()
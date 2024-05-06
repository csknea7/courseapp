from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20)
    page_number = models.IntegerField()
    publish_data = models.DateTimeField()
    stock = models.IntegerField()

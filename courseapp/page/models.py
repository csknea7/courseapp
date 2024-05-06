from django.db import models


class Category(models.Model):
    field = models.CharField(max_length=50)

    class Meta:
        db_table = "category_table"

    def __str__(self):
        return self.field


class Destination(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)

    class Meta:
        db_table = "destination_table"
        ordering = ['name', 'title', 'description', 'category']

    def __str__(self):
        return self.name


from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField()
    isActive = models.BooleanField()

    def __str__(self):
        return f"{self.title} {self.description} {self.imageUrl} {self.date} {self.isActive}"


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)
    # from courses.models import Course
    # kurs1 = Course(title="javascript", description="kurs bilgisi", imgaeUrl="1.jpg", date=datetime.now(), isActive=1)


class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    is_active = models.BooleanField(default=False)
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class UploadModel(models.Model):
    image = models.ImageField(upload_to="image")

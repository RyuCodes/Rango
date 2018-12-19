from django.db import models

# Create your models here.

class Category(models.Model):
    #unique means that only one instance of the particular value may exist int he entire model
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        #sets the plural name as "Categories".  Overides singular + 's'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Page (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    #URLField stores resource URL
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

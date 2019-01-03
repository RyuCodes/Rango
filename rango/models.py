from django.db import models
from django.contrib.auth.models import User

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

class UserProfile (models.Model):
    #Links UserProfile to User model instance. Required
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional attributes to include
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    #override __str__

    def __str__(self):
        return self.user.username

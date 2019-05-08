from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

class Image(models.Model):
    image_name = models.CharField(max_length=60)
    image_description = models.CharField(max_length=255)
    image_date = models.DateTimeField(auto_now_add=True)
    # Foreign keys
    image_location = models.ForeignKey('Location')
    image_category = models.ManyToManyField('Category')
    image_user = models.ForeignKey('User')

    @classmethod
    def search_by_category(cls,search_term):
        image_search = cls.objects.filter(image_category__icontains=search_term)
        return image_search

class Location(models.Model):
    location_name = models.CharField(max_length=30)

class Category(models.Model):
    category_name = models.CharField(max_length=30)
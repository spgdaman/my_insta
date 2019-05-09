from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=60)
    image_description = models.CharField(max_length=255)
    image_date = models.DateTimeField(auto_now_add=True)
    # Foreign keys
    image_location = models.ForeignKey('Location')
    image_category = models.ManyToManyField('Category')
    image_user = models.ForeignKey('User')

    @classmethod
    def save_image(cls):
        image_saved = cls.objects.save()
        return image_saved

    @classmethod
    def delete_image(cls,image_id):
        image_deleted = cls.objects.filter(id=image_id).delete()
        return image_deleted

    @classmethod
    def update_image(cls,image_id,image_name):
        image_updated = cls.objects.filter(id=image_id).update(image_name=image_name)
        return image_updated

    @classmethod
    def get_image_by_id(cls,id):
        get_image = cls.objects.filter(id=id)
        return get_image
    
    @classmethod
    def search_image(cls,category):
        image_searched = cls.objects.filter(image_category=category)
        return image_searched

    @classmethod
    def filter_by_location(cls,location):
        image_location = cls.objects.filter(image_location=location)
        return image_location

class Location(models.Model):
    location_name = models.CharField(max_length=30)

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    @classmethod
    def search_by_category(cls,search_term):
        category_search = cls.objects.filter(category_name__icontains=search_term)
        return category_search
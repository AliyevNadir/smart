from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(blank=True, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    description = RichTextField()
    image = models.ImageField(upload_to='book')
    is_home = models.BooleanField()
    slug = models.SlugField(blank=True, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    


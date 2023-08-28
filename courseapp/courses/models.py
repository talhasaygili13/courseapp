from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, default='', null=False, unique=True, db_index=True)

    def __str__(self):
        return f'{self.name}'
class Course(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, default='')
    description = RichTextField()
    image = models.ImageField(upload_to='images', default='')
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default='',blank=True, null=False, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)

    def __str__(self):
        return f'{self.title} {self.date}'

class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    is_active = models.BooleanField(default=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'



class UploadModel(models.Model):
    image = models.ImageField(upload_to='images')
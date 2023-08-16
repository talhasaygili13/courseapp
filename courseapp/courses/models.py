from django.db import models
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, default='', null=False, unique=True, db_index=True)

    def __str__(self):
        return f'{self.name}'
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default='',blank=True, null=False, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)

    def __str__(self):
        return f'{self.title} {self.date}'

from django.contrib import admin
from .models import Course,Category

# Register your models here.


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'isActive', 'slug',)
    list_display_links = ('title', 'slug')
    list_filter = ('isActive',)
    list_editable = ('isActive',)
    search_fields = ('title',)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', 'slug')
    search_fields = ('name',)
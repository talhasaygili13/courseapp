from django.contrib import admin
from .models import Course,Category

# Register your models here.


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'isActive', 'slug','category_list',)
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ('isActive',)
    list_editable = ('isActive',)
    search_fields = ('title',)
    def category_list(self, obj):
        html = ''
        for category in obj.categories.all():
            html += category.name
            if  obj.categories.count() >= 2:
                html += ', '
        return html.rstrip(', ')

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'slug','course_count')
    list_display_links = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',),}
    search_fields = ('name',)
    
    def course_count(self, obj):
        return obj.course.count()
from django.contrib import admin
from .models import Course, Category, Slider



@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'isActive','isHome', 'slug','category_list',)
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ('isActive','isHome',)
    list_editable = ('isActive','isHome',)
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
    list_display = ('name', 'slug',)
    list_display_links = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',),}
    search_fields = ('name',)

    def course_count(self, obj):
        return obj.course.count()

admin.site.register(Slider)
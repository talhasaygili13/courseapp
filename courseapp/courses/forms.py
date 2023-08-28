from django import forms

from courses.models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug')
        labels = {
            'title': 'Title: ',
            'description': 'Course Description: ',
            'slug': 'Slug: ',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug', 'categories', 'isActive', 'isHome')
        labels = {
            'title': 'Title: ',
            'description': 'Course Description: ',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'isActive': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'isHome': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class UploadForm(forms.Form):
    image = forms.ImageField()
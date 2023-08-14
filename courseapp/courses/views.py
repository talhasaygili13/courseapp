from datetime import date
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course,Category

data = {
    'programming':'Programlama kategorisine ait kurslar',
    'web-development':'Web gelistirme kategorisine ait kurslar',
    'mobile-app':'Mobil kategorisine ait kurslar',
}

db = {
    'courses':[
        {
            'title': 'Javascript Course',
            'description': 'Javascript course description',
            'imageUrl': 'js-course.jpg',
            'slug': 'javascript-course',
            'date': date(2023, 10, 12),
            'isActive': True,
            'isUpdated':True
        },
        {
            'title': 'Python Course',
            'description': 'Python course description',
            'imageUrl': 'py-course.png',
            'slug': 'python-course',
            'date': date(2022, 12, 12),
            'isActive': True,
            'isUpdated':True
        },
        {
            'title': 'Web Development Course',
            'description': 'Web development course description',
            'imageUrl': 'wd-course.jpg',
            'slug': 'web-development-course',
            'date': date(2023, 9, 2),
            'isActive': True,
            'isUpdated':False
        }
    ],
    'categories':[
        {'id': 1, 'name':'Programming', 'slug':'programming'},
        {'id': 2, 'name': 'Web Development', 'slug': 'web-development'},
        {'id': 3, 'name': 'Mobile Application', 'slug': 'mobile-app' },
        ]
}

def index(request):
    courses = Course.objects.filter(isActive=1)
    categories = Category.objects.all()
    return render(request, 'courses/index.html', {
        'categories': categories,
        'courses': courses,
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course' : course
    }
    return render(request, 'courses/details.html', context)


def programlama(request):
    return HttpResponse('Programlama kurs Listesi')

def mobil_uygulamalar(request):
    return HttpResponse('Mobil uygulamalar kurs Listesi')

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'courses/courses.html', {
            'category' : category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound('Yanlis kategori secimi')

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound('Yanlis kategori secimi')
    category_name = category_list[category_id - 1]
    redirect_url = reverse('courses_by_category', args=[category_name])
    return redirect(redirect_url)
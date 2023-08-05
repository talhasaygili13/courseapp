from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('First page')

def kurslar(request):
    return HttpResponse('Kurs Listesi')
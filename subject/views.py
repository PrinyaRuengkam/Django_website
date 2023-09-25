from django.shortcuts import render
from .models import subject

def render_subject_page(request, template_name, category):
    context = {}
    subjects = subject.objects.filter(class_category=category)
    context['subjects'] = subjects
    return render(request, template_name, context)

def index(request):
    subjects = subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def general(request):
    return render_subject_page(request, 'home2.html', 1)

def elective(request):
    return render_subject_page(request, 'home3.html', 2)

def technical(request):
    return render_subject_page(request, 'home4.html', 3)

from django.http import StreamingHttpResponse

def stream_subject_page(request, template_name, category):
    subjects = subject.objects.filter(class_category=category)
    response = StreamingHttpResponse(
        render(request, template_name, {'subjects': subjects})
    )
    return response







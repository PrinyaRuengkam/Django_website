from django.shortcuts import render

from . import models
# Create your views here.

def index(request):
    context = {}
    
    subject = models.subject.objects.all()
    context['subjects'] = subject
    
    
    return render(request, 'home.html', context)
    
    
def about(request):
    return render(request, 'about.html')
    




def general(request):
    context = {}
    
    subject = models.subject.objects.filter(class_category=1)
    context['subjects'] = subject
    
    return render(request, 'home2.html',context)




def elective(request):
    context = {}
    
    subject = models.subject.objects.filter(class_category=2)
    context['subjects'] = subject
    
    return render(request, 'home3.html',context)



def technical(request):
    context = {}
    
    subject = models.subject.objects.filter(class_category=3)
    context['subjects'] = subject
    
    return render(request, 'home4.html',context)






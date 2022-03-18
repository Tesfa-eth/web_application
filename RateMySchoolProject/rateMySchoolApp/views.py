import imp
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Universities

# Create your views here.

def index(request):
    return render(request,'rateMySchool/index.html')

def college_rating(request):
    posts = Post.objects.all()
    univeristies = Universities.objects.all()

    context = {
        'posts': posts,
        'universities' : univeristies
    }
    return render(request, 'rateMySchool/collegeRating.html', context)
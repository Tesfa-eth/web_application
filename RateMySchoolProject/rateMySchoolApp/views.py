import imp
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Universities
import wikipediaapi
# from .wikiAPI import get_summary # import not working

# Create your views here.

def index(request):
    return render(request,'rateMySchool/index.html')

def get_summary(name):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(name)
    if page_py.exists():
        return page_py.summary
    else:
        return 'Wiki summary not found'
        

def college_rating(request):
    posts = Post.objects.all()
    univeristies = Universities.objects.all()

    if 'q' in request.GET:
        q = request.GET['q']
        data = Universities.objects.filter(name__icontains=q)
        data = data[0]
        summary = get_summary(data)
    else:
        data = ''
        summary = ''
    
    context = {
        'posts': posts,
        'universities' : univeristies,
        'queryUNI' : data,
        'wiki_summary': summary
    }
    return render(request, 'rateMySchool/collegeRating.html', context)
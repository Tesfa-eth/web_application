import imp
from unicodedata import name
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

    if 'collegeQuery' in request.GET:
        q = request.GET['collegeQuery']
        crude_data = Universities.objects.filter(name__icontains=q)
        query_post = Post.objects.filter(ratedBody=crude_data[0])
        #print(crude_data[0])
        #print(query_post)
        data = crude_data[0]
        summary = get_summary(data)
    else:
        data = ''
        summary = ''
        query_post = ''
    
    context = {
        'posts': query_post,
        'universities' : univeristies,
        'queryUNI' : data,
        'crudeQueryResult': data,
        'wiki_summary': summary
    }
    return render(request, 'rateMySchool/collegeRating.html', context)
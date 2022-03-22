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
        
def matchRatings(data):
    matchedData = []
    lable = []
    #if 5 in data:
    lable.append("5-star")
    matchedData.append(data.count(5))
    #if 4 in data:
    lable.append("4-star")
    matchedData.append(data.count(4))
    #if 3 in data:
    lable.append("3-star")
    matchedData.append(data.count(3))
    #if 2 in data:
    lable.append("2-star")
    matchedData.append(data.count(2))
    #if 1 in data:
    lable.append("1-star")
    matchedData.append(data.count(1))
    
    return lable, matchedData
def Average(lst):
    return sum(lst) / len(lst)

def college_rating(request):
    posts = Post.objects.all()
    univeristies = Universities.objects.all()

    graph_data = []
    lable = []
    
    
    if 'collegeQuery' in request.GET:
        q = request.GET['collegeQuery']
        crude_data = Universities.objects.filter(name__icontains=q)
        query_post = Post.objects.filter(ratedBody=crude_data[0])
        #print(crude_data[0])
        #print(query_post)
        data = crude_data[0]
        summary = get_summary(data)
        # chart
        queryPost = Post.objects.filter(ratedBody=crude_data[0]).order_by('-rate_stars')
        for post in queryPost:
             graph_data.append(post.rate_stars)
        
        average_rating = Average(graph_data)
        lable, graph_data = matchRatings(graph_data)
        

    else:
        data = ''
        summary = ''
        query_post = ''
        average_rating = ''
    print(graph_data, lable)
    context = {
        'posts': query_post,
        'universities' : univeristies,
        'queryUNI' : data,
        'crudeQueryResult': data,
        'wiki_summary': summary,
        'graph_data': graph_data,
        'lable': lable,
        'average_rating': average_rating
    }
    return render(request, 'rateMySchool/collegeRating.html', context)
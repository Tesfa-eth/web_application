import imp
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Universities
import wikipediaapi
# from .wikiAPI import get_summary # Todo: import needs to be fixed

# Create your views here.
def index(request):
    """render the main page"""
    return render(request,'rateMySchool/index.html')

def get_summary(name):
    """takes the title of university and returns a wiki summery"""
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(name)
    if page_py.exists():
        return page_py.summary
    else:
        return 'Wiki summary not found'
        
def matchRatings(data):
    """matches ratings data to lables"""
    matchedData = []
    lable = []
    lable.append("5-star")
    matchedData.append(data.count(5))
    lable.append("4-star")
    matchedData.append(data.count(4))
    lable.append("3-star")
    matchedData.append(data.count(3))
    lable.append("2-star")
    matchedData.append(data.count(2))
    lable.append("1-star")
    matchedData.append(data.count(1))
    
    return lable, matchedData

def Average(lst):
    """calculate average rating"""
    if len(lst) > 0:
        return sum(lst) / len(lst)
    else:
        return 0

def college_rating(request):
    """renders college rating page"""

    # variables
    data = ''
    summary = ''
    query_post = ''
    average_rating = ''

    # get university list for search recommendation
    univeristies = Universities.objects.all()
    graph_data = []
    lable = []
    if 'collegeQuery' in request.GET:
        q = request.GET['collegeQuery']
        crude_data = Universities.objects.filter(name__icontains=q)
        if len(crude_data) != 0: # if the search succeeds
            query_post = Post.objects.filter(ratedBody=crude_data[0])
            # debug
            # print(crude_data[0])
            # print(query_post, len(query_post), "query post")
            data = crude_data[0]
            summary = get_summary(data)
            # chart
            queryPost = Post.objects.filter(ratedBody=crude_data[0]).order_by('-rate_stars')
            for post in queryPost:
                graph_data.append(post.rate_stars)
            
            average_rating = Average(graph_data)
            lable, graph_data = matchRatings(graph_data)
        
    #print(graph_data, lable)
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
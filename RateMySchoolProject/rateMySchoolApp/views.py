from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'rateMySchool/index.html')

def college_rating(request):
    return render(request, 'rateMySchool/collegeRating.html')
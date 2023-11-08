from django.shortcuts import render
from django.http import HttpResponse
def silk(request):
    return HttpResponse('<h1><marquee>we are not talking about dairy milk silk</marquee></h1>')
    

# Create your views here.

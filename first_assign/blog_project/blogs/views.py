from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

def root(request):
    return HttpResponseRedirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return HttpResponseRedirect('/')
def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    HttpResponseRedirect('/blogs')

def json_response(request):
    data = {
        'title': 'sample blog title',
        'content':'sample blog content'
    }
    return json_response(data)
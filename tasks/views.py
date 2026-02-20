from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Task Management system")

def contact(request):
    return HttpResponse("This is contact page")
        
def showTask(request):
    return HttpResponse("This is our task page")
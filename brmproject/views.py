from django.shortcuts import render
from django.http import HttpResponse
def helloView(request):
    return HttpResponse("helloView")

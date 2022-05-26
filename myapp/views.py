from django.shortcuts import render
from django.http import HttpResponse

def message(requests):
    return HttpResponse("This is Training.")

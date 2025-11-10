from django.shortcuts import render
from django.http import HttpResponse

def activity(request):
    return HttpResponse("Activity app index")
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "missions/home.html", {'message': 'hi, there.'} )

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'header_text': "About page"} 
    return render(request, "rango/about.html", context_dict)

from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def home(request):
    d = {}
    return render(request, 'home.html', d)

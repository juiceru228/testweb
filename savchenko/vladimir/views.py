from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def name(request):
	return render(request, "name.html")

def group(request):
	return render(request, "group.html")

def age(request):
	return render(request, "age.html")

def common(request):
	return render(request, "common.html")

def main(request):
	return render(request, "main.html")

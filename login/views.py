from django.shortcuts import render
#1from django.http import HttpResponse

# Create your views here.

#1def sign(request):
#1	return HttpResponse("Hello")

def sign(request):
	return render(request,'login/login.html')

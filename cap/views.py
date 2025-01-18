from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cap(request):
    return render(request, "cap/cap.html")
def home(request):
    return HttpResponse("i am home page of cap")
def about(request):
    re
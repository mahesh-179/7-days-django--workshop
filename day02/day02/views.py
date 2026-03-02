from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse(" MAHESH | CHAI PAGE ")
    return render(request,"website/index.html")

def about(request):
    return HttpResponse(" MAHESH | ABOUT PAGE ")
def contact(request):
    return HttpResponse(" MAHESH | CONTACT PAGE ")
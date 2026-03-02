from django.shortcuts import render

# Create your views here.
def all_chai(request):
    return render(request,"firstapp/all_chai.html")
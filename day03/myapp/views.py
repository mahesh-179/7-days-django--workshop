from django.shortcuts import render

# Create your views here.
def chai_list(request):
    return render(request,"myapp/index.html")
# from django.shortcuts import render
# from .models import ChaiVariety
# from django.shortcuts import get_object_or_404
# # Create your views here.
# def menu(request):
#     items=ChaiVariety.objects.all()
#     return render(request, "menu/menu.html",{'items':items})

# def order_confirmation(request,chai_id):
#     chai=get_object_or_404(ChaiVariety,pk=chai_id)
#     return render(request,"menu/confirmation.html",{'chai':chai})
from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety,ChaiReview,Store
from .forms import ChaiVarietyForm
# Display all menu items
def menu(request):
    items = ChaiVariety.objects.all()
    reviews = ChaiReview.objects.all()
    branches=Store.objects.all()
    context = {
        'items': items,
        'reviews': reviews,
        'branches':branches,
    }
    return render(request, "menu/menu.html", context)

# Order confirmation page
def order_confirmation(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, "menu/confirmation.html", {'chai': chai})

def store_location(request):
     branches=Store.objects.all()
     context = {
        'branches':branches,
    }
     return render(request, "menu/location.html", context)

def chai_stores_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
        chai_variety =form.cleaned_data['chai_variety']

    return render(request,"menu/chai_stores.html",{'stores':stores})
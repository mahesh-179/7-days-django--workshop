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
from .models import ChaiVariety,ChaiReview

# Display all menu items
def menu(request):
    items = ChaiVariety.objects.all()
    reviews = ChaiReview.objects.all()
    context = {
        'items': items,
        'reviews': reviews
    }
    return render(request, "menu/menu.html", context)

# Order confirmation page
def order_confirmation(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, "menu/confirmation.html", {'chai': chai})

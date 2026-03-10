from django.shortcuts import render

def home(request):
    return render(request, "layout.html")


def menu(request):
    return render(request, "menu/menu.html")


def about(request):
    return render(request, "about/about.html")

def contact(request):
    return render(request, "contact/contact.html")
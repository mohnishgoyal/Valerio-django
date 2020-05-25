from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Valerio_app/index.html')

def app(request):
    return render(request, 'Valerio_app/pages/app.html')

def blog(request):
    return render(request, 'Valerio_app/pages/blog.html')

def contact(request):
    return render(request, 'Valerio_app/pages/contact.html')

def partners(request):
    return render(request, 'Valerio_app/pages/partners.html')

def privacy(request):
    return render(request, 'Valerio_app/pages/privacy.html')

def team(request):
    return render(request, 'Valerio_app/pages/team.html')

def termsofuse(request):
    return render(request, 'Valerio_app/pages/termsofuse.html')

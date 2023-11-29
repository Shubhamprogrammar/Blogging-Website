from django.shortcuts import render
from home.models import Contact
from datetime import datetime

# Create your views here.
def index(request):
    context = {"college":"SIES(NERUL) College of Arts, Science and Commerce"}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def education(request):
    return render(request,"education.html")

def social(request):
    return render(request,"social.html")

def news(request):
    return render(request,"news.html")

def career(request):
    return render(request,"career.html")

def disclaimer(request):
    return render(request,"disclaimer.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("Email1")
        feed = request.POST.get("feed")
        contact = Contact(name=name, email=email, feedback=feed, date = datetime.today())
        contact.save()
    return render(request,"contact.html")

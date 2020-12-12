from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/)")
    context = {'name': 'Henry', 'project': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse("This is my about page (/about)")
    return render(request, 'about.html')

def credentials(request):
    #return HttpResponse("This is my about page (/about)")
    return render(request, 'about.html')


def contact(request):
    if request.method=="POST":
        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been written to the data base")

    #return HttpResponse("This is my contact page (/contact)")
    return render(request, 'contact.html')

def projects(request):
    #return HttpResponse("This is my projects page (/projects)")
    return render(request, 'projects.html')

def search(request):
    #return HttpResponse("This is my search results page (/search)")
    return render(request, 'search.html')




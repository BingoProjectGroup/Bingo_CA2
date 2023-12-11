from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


from.models import Book
form.forms import CreateUserForm
# Create your views here.

def registerPage(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'register.html', context)

def loginPage(request):
    context={}
    return render(request,'login.html', context)


def helloView(request):
    books=Book.objects.all()
    return render(request,"viewbook.html",{"books":books})
def addBookView(request):
        
    return render(request,"addbook.html")

def addBook(request):
     if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        print(t,p)
        book=Book()
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')

def editBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')   


def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    print(book)
    return render(request,"edit-book.html",{"book":book})  

def deleteBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/') 

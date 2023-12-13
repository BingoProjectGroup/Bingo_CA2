from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from.models import Book
from.forms import CreateUserForm
# Create your views here.

def registerPage(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Hi'+ user + ' Registration is Succesful!')
            return redirect('/login')

    context={'form':form}
    return render(request,'register.html', context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('helloView')
        else:
            messages.info(request,'Email or Password is incorrect')


    context={}
    return render(request,'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login')
def helloView(request):
    books=Book.objects.all()
    return render(request,"viewbook.html",{"books":books})
    
@login_required(login_url='/login')
def addBookView(request):
        
    return render(request,"addbook.html")

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def editBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')   

@login_required(login_url='/login')
def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    print(book)
    return render(request,"edit-book.html",{"book":book})  

@login_required(login_url='/login')
def deleteBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/') 

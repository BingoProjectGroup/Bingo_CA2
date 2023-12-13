from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from.models import Book
from.forms import CreateUserForm
from.decorators import unauthenticated_user,admin_only,allowed_users
# Create your views here.

@unauthenticated_user
def registerPage(request):
    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Hi '+ username + ', Registration is Succesful!')
            return redirect('/login')

    context={'form':form}
    return render(request,'register.html', context)


@unauthenticated_user
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

def userPage(request):
    context={}
    return render(request, 'user.html',{"books":books})

@login_required(login_url='/login')
@admin_only
def helloView(request):
    books=Book.objects.all()
    return render(request,"viewbook.html",{"books":books})
    
@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def addBookView(request):
        
    return render(request,"addbook.html")

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    print(book)
    return render(request,"edit-book.html",{"book":book})  

@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
def deleteBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/') 

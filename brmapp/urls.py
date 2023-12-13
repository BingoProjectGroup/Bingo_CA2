
from django.contrib import admin
from django.urls import path,include,re_path
from .views import helloView,registerPage,loginPage,addBookView,addBook,editBookView,editBook,deleteBookView

urlpatterns = [
    
    path("",helloView, name=helloView),
    path("register/",registerPage),
    path("login/",loginPage),
    path("add-book/",addBookView),
    path("add-book/addbookdata",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book/",deleteBookView),
    
    
    
    
    
]

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime,timedelta,date
from .models import IssueBook, UserExtend,AddBook


def addbook(request):
    Book = AddBook.objects.all()
    return render(request,'addbook.html',{'Book':Book})

  
def AddBookSubmission(request):
    if request.session.has_key('is_logged'):
       if request.method == "POST":
          user_id = request.session["user_id"]
          user1 = User.objects.get(id=user_id
          bookid = request.POST["bookid"]
          bookname = request.POST["bookname"]
          subject = request.POST["subject"]
          category = request.POST["category"]
          add = AddBook(user = user1,bookid=bookid,bookname=bookname,subject=subject,category=category)
          add.save()
          Book = AddBook.objects.all()
          return render(request,'dashboard.html',{'Book':Book})
   return redirect('/')
  
  
def bookissue(request):
    return render(request,'bookissue.html')

  
def issuebooksubmission(request):
     if request.method == 'POST':
          user_id = request.session["user_id"]
          user1 = User.objects.get(id=user_id)
          studentid = request.POST['studentid']
          book1 = request.POST['book1']
          store = AddBook.objects.filter(bookid=book1)
            
          def get_category(addbook):
              if addbook.category == "Not-Issued":
                  addbook.category = "Issued"
                  obj = IssueBook(user=user1,studentid=studentid,book1=book1)
                  obj.save()
                  addbook.save()
              else:
                  messages.error(request," Book already issued !!!")
          category_list = list(set(map(get_category,store)))         
          Issue = IssueBook.objects.all()
          return render(request,'bookissue.html',{'Issue':Issue})
     return redirect('/')

    

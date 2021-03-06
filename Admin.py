from django.contrib import admin
from .models import AddBook,IssueBook
from django.contrib.sessions.models import Session
admin.site.register(Session)
from .models import UserExtend
admin.site.register(UserExtend)


class AddBook_Admin(admin.ModelAdmin):
    list_display = ("user","bookid","bookname","subject","category")
admin.site.register(AddBook,AddBook_Admin)

class IssueBookAdmin(admin.ModelAdmin):
    list_display = ("user","book1","studentid")
admin.site.register(IssueBook,IssueBookAdmin)

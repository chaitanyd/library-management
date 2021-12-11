from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addbook/',views.addbook,name='addbook'),
    path('bookissue/',views.bookissue,name='bookissue'),

]

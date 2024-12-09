from django.urls import path
from .views import *

urlpatterns = [
    path('add/', AddBlog.as_view(), name='add_blog'),
    path('<str:blogid>/', BlogView, name='blog'),
    path('',Blogs, name='blogs')
]

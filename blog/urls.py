from django.urls import path
from .views import *

urlpatterns = [
    path('add/', AddBlog.as_view(), name='add_blog'),  # Home page URL
    path('<str:blogid>', BlogView, name='blog'),  # Home page URL
]

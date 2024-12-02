from django.urls import path
from .views import home, login

urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('login/', login.as_view(), name='login'),  # Login page URL
]

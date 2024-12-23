from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),  # Home page URL
    path('login/', Login.as_view(), name='login'),  # Login page URL
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', Signup.as_view(), name='signup'),
    path('join', Join.as_view(), name='join'),
    path('contact_us', Contact, name="contact"),
    path('privacy_policy', Privacy, name="privacy"),
    path('rent_a_bike', Rent, name="rent")
]

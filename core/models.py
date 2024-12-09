from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

class MembershipDetails(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="membership")
    upi_transactionid = models.CharField(max_length=12)
    membership_status = models.CharField(max_length=10)
    valid_until = models.DateTimeField(auto_now_add=True)
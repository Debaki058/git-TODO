from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings
import secrets

class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    # is_active = True
    USERNAME_FIELD= ("email")
    REQUIRED_FIELDS= ["username"]


    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        # Set is_active to True if the user is a staff member
        if self.is_staff:
            self.is_active = True
        super().save(*args, **kwargs)
    


class OtpToken(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="otps")
   otp_code = models.CharField(max_length=6, default=secrets.token_hex(3))
   otp_created_at = models.DateTimeField(auto_now_add=True)
   otp_expires_at = models.DateTimeField(blank=True, null=True)
   
   def __str__(self):
        return self.user.username
   


class Student(models.Model):
    roll=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
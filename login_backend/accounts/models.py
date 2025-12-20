from django.db import models
from django.contrib.auth.models import User #creates User model that has username, password, email etc.
# Create your models here.
class addons(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#creates a one to one relationship with User model
    #additional fields in our <form>
    phone = models.CharField(max_length=15, blank=True)
    about = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"addons for {self.user.username}"
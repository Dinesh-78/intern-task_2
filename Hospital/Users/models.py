from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.urls import reverse
# Create your models here.


class User(AbstractUser):
   doctor= models.BooleanField('Doctor', default=False)
   patient = models.BooleanField('Patient', default=False)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
class hcategory(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class blog(models.Model):
    title=models.CharField(max_length=255)
    Category=models.ForeignKey(hcategory,on_delete=models.CASCADE,null=True)
    Summary=models.TextField(null=True)
    Content=models.TextField()
    draft=models.BooleanField('draft',default=False)
    b_image=models.ImageField(null=True,blank=True,upload_to="img/")



    def __str__(self):
        return self.title 
    
    # def get_absolute_url(self):
    #     return reverse('doctorpage')
    
    

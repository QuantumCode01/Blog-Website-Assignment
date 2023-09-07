from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    content= models.TextField()
    publicationdate=models.DateField(auto_now_add=True)
    name=models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    image = models.ImageField(upload_to='eventimages',null=True)


    def __str__(self):
       return self.title
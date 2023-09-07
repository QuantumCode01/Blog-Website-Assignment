from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Post


class UserRegisterationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))  
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        # widgets to apply bootsraps form control class to each filed of user registeration form
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            } 
        
class UserAuthenticationForm(AuthenticationForm):
   password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
   username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'})) 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image']
        labels={'title':"Title",'content':'Content','publicationdate':"Publication Date",'image':'Post Image'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
        'content':forms.Textarea(attrs={'class':'form-control'}),'publicationdate':forms.DateInput(attrs={'type':'date','placeholder':'mm-dd-yyyy','class':'form-control'})}

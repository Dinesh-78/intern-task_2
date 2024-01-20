from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,blog,hcategory

class Profilepic(forms.ModelForm):
    profile=forms.ImageField(label='profile_pic')



class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('firstname','lastname','username', 'email', 'password1', 'password2','address', 'doctor', 'patient')

class AddPost(forms.ModelForm):
    Category = forms.ModelChoiceField(queryset=hcategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}))
    class Meta:
        model =blog
        fields=('title','Category','Summary','Content','b_image','draft')
        labels={
            'Title1':'',
            'Category':'',
            'Summary':'',
            'Content':'',
            'blog-image':'',
            'draft':'',
        }
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'TITLE'}),
            'Summary': forms.TextInput(attrs={'class':'form-control','placeholder':'SUMMARY'}),
            'Content': forms.TextInput(attrs={'class':'form-control','placeholder':'Content'}),
            
        }

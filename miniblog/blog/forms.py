from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import blog_post 
from django_ckeditor_5.widgets import CKEditor5Widget


class BlogPost_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["desc"].required = False
    class Meta:
        model = blog_post
        fields = ['title', 'desc','category']
        widgets = {
            "desc": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }

class Register_form(UserCreationForm):
    password1 = forms.CharField(
        label= "Password",
        help_text= "Your password must contain at least 8 characters.",
        widget= forms.PasswordInput,   
    )

    password2 = forms.CharField(
        label= "Confirm Password",
        help_text= "Enter the same password as before, for verification..",
        widget= forms.PasswordInput,
        
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {'first_name': 'First Name' ,'last_name':'Last Name', 'email': 'Email Id'}
        
class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1']
        
        

# For news latter subscription 
class SubscriptionsForm(forms.Form):
    sub_email = forms.EmailField(label='Email', max_length=200)


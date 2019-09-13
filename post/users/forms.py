from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User
class UserForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text = None


class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image':'Suratyn'
        }     
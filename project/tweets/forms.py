
from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [ 'text', 'photo']
        
class UserRegister(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
        
def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ❌ Remove help text
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
from django import forms 
from .models import tweets

class TweetForm(forms.Modelform):
    class Meta:
        model = tweets
        fields = ['user','text','photo']
from django import forms
from django.forms import ModelForm
from.models import *

class AppForm(forms.ModelForm):
    #app = forms.CharField(widget= forms.TextInput(attrs={'placeholder': ' add new list'}))
    class Meta:
        model= App
        fields = ['title']
        exclude = "__all__"
    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "add new list"



class AppUpdateForm(forms.ModelForm):
    
    class Meta:
        model= App
        fields = '__all__'


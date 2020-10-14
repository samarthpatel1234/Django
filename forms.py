from django import forms
# import GeeksModel from models.py
from .models import Person

# create a ModelForm
class PersonForm(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Person
        fields = "__all__"

class user(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput())
    class Meta:
        model = Person
        fields = ['user_name',]


class PersonFormset(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Person
        fields = "__all__"

# creating a form
class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(
        help_text="Enter 6 digit roll number"
    )
    password = forms.CharField(widget=forms.PasswordInput())
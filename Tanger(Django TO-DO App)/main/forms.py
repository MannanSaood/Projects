from django import forms
from .models import todoList,Item

class CreateNewList(forms.Form):
    name = forms.CharField(max_length=200)
    check = forms.BooleanField(required=True)

class CreateNewItem(forms.Form):
    text = forms.CharField(max_length=200)

class UpdateItem(forms.ModelForm):
    class Meta:
        model = Item
        text = forms.CharField(max_length=200)
        fields = ['text','complete']

class UpdateList(forms.Form):
    name = forms.CharField(max_length=200)
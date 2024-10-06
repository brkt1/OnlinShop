from django import forms
from .models import Item

 
class newItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'price', 'description','telegram_link','category','image')

class EditItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'price', 'description','telegram_link','category','image','is_sold')
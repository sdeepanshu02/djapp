from django import forms
from .models import Menu

class addMenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('item_name', 'price',)
        labels = { 'item_name': ('Menu Item'), }

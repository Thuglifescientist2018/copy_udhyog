from django import forms
from .models import Sales


class SalesModelForm(forms.ModelForm):
    class Meta:
        model = Sales
        labels = {
            'product_name': 'सामान को नाम',
            'price': 'बेचेको दाम',
            'quantity': 'कती वटा?',
            'sold_to': 'कता बेचेको?'
        }
        fields = ["product_name", "price", "quantity", "sold_to"]

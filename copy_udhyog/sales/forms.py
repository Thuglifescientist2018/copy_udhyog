from django import forms
from .models import Sales


class SalesModelForm(forms.ModelForm):
    class Meta:
        model = Sales
        labels = {
            'product_name': 'सामान को नाम',
            'price': 'बेचेको दाम',
            'quantity': 'कती वटा?',
            'sold_to': 'कता बेचेको?',
            "date": "मिती",
        }
        fields = ["product_name", "price", "quantity", "sold_to", "date"]

    def clean_product_name(self, *args, **kwargs):
        instance = self.instance
        product_name = self.cleaned_data.get("product_name")
        qs = Sales.objects.filter(product_name__iexact=product_name)
        if instance is not None:  # we ignore the old instance update the data due to which
            # we are not gonna be getting title already exists error i think slug updates fine after adding instance=obj in the update view
            qs = qs.exclude(pk=instance.pk)  # id = instance of id
        if qs.exists():
            raise forms.ValidationError(
                "This Product name has been already taken")
        return product_name

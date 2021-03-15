from django import forms
from .models import Purchases


class PurchasesModelForm(forms.ModelForm):
    class Meta:
        model = Purchases
        labels = {
            'product_name': 'सामान को नाम',
            'price': 'किनेको मुल्य',
            'quantity': 'कती वटा ',
            'bought_from': 'कताबाट किनेको ?'
        }
        fields = ["product_name", "price", "quantity", "bought_from"]

    def clean_product_name(self, *args, **kwargs):
        instance = self.instance
        product_name = self.cleaned_data.get("product_name")
        qs = Purchases.objects.filter(product_name__iexact=product_name)
        if instance is not None:  # we ignore the old instance update the data due to which
            # we are not gonna be getting title already exists error i think slug updates fine after adding instance=obj in the update view
            qs = qs.exclude(pk=instance.pk)  # id = instance of id
        if qs.exists():
            raise forms.ValidationError(
                "This Product name has been already taken")
        return product_name

from admins.models import Prodcuts
from django import forms

class UploadForm(forms.ModelForm):
    class Meta:
        model = Prodcuts
        fields = ('category', 'product_name', 'vendor_name', 'color', 'price', 'featuers', 'images')
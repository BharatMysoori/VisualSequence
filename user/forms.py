from django import forms

from user.models import RegisterModel, Purchase, ReviewModel


class RegisterForms(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields=("firstname","lastname","userid","password","email","gender","mblenum","category")

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('quantity',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ('review',)
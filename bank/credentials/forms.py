# forms.py
from django import forms
from .models import District, Branch
from .models import BankAccountApplication

class DistrictBranchForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select a District")
    branch = forms.ModelChoiceField(queryset=Branch.objects.none(), empty_label="Select a Branch")

class BranchForm(forms.Form):
    district = forms.ChoiceField(choices=[], required=False)
    branch = forms.ChoiceField(choices=[], required=False)

class BankAccountApplicationForm(forms.ModelForm):
    class Meta:
        model = BankAccountApplication
        fields = '__all__'

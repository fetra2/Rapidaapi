from django import forms

class TarifForm(forms.Form):
    zone = forms.IntegerField(label='Zone')
    poids = forms.IntegerField(label='Poids')
from django import forms
from .models import Moeda,Pais

class MoedaForm(forms.ModelForm):
    class Meta:
        model = Moeda
        fields = ['codigo', 'tipo','nome','simbolo','compra','venda','data']

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nome']
                
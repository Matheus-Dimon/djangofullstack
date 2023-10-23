from .models import Product
from django import forms


class ProdutoCadastroForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['descrição', 'marca', 'modelo', 'preço', 'tipo']
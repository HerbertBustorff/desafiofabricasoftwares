from django.forms import ModelForm
from .models import Transacao



class TransacaoForm(ModelForm):
    class Meta: 
        model = Transacao
        fields = ['valor', 'data', 'descricao', 'observacoes', 'categoria']


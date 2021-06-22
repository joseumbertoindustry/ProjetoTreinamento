from django import forms
from django.utils.safestring import mark_safe

class FormLogin(forms.Form):  
  email = forms.EmailField(label="E-mail", max_length=100, 
    widget=forms.TextInput(attrs={'class':'form-control', 'id': 'email'})
  )
  password = forms.CharField(label="Senha", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'id': 'pass'}))

class FormIdCidadeTipo(forms.Form):
  idCidade = forms.IntegerField(label="ID Cidade", 
    widget=forms.TextInput(attrs={'class':'form-control', 'id': 'idcidade'})
  )

  idTipo = forms.IntegerField(label="ID Tipo", 
    widget=forms.TextInput(attrs={'class':'form-control', 'id': 'idtipo'})
  )

class FormIdBairro(forms.Form):
  idBairro = forms.IntegerField(label="ID Bairro", 
    widget=forms.TextInput(attrs={'class':'form-control', 'id': 'idbairro'})
  )

  bairro = forms.CharField(label="Bairro", max_length=100, 
    widget=forms.TextInput(attrs={'class':'form-control', 'id': 'bairro'})
  )
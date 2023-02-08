from django import forms


class usuarioFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
  
class propiedadesFormulario(forms.Form):

    pais = forms.CharField()
    provincia = forms.CharField()
    ciudad = forms.CharField()
    metrosCubiertos = forms.FloatField()

class inversoresFormulario(forms.Form):

    email = forms.EmailField()
    divisa = forms.CharField() 
    cantInvertir = forms.IntegerField()

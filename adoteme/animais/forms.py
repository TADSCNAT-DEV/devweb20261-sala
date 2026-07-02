from django import forms

class TipoAnimalForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome do tipo de animal'}))
    
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if 'xxx' in nome.lower():
            raise forms.ValidationError('Nome contém conteúdo inapropriado.')
        return nome
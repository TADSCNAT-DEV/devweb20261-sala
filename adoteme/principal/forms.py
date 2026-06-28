from django import forms
class ContatoForm(forms.Form):
    titulo=forms.CharField(label='Título', max_length=100,
                           widget=forms.TextInput(attrs={'class':'input','placeholder':'Título'}))
    email=forms.EmailField(label='E-mail', max_length=100,
                           widget=forms.EmailInput(attrs={'class':'input','placeholder':'E-mail'}))
    mensagem=forms.CharField(label='Mensagem', max_length=1000,
                           widget=forms.Textarea(attrs={'class':'textarea','placeholder':'Mensagem'}))
    
    def clean_mensagem(self):
        mensagem = self.cleaned_data.get('mensagem', '')
        error_messages = []
        if 'xxx' in mensagem.lower():
            error_messages.append(forms.ValidationError('Mensagem contém conteúdo inapropriado.'))
        if len(mensagem) < 10:
            error_messages.append(forms.ValidationError('A mensagem deve ter no mínimo 10 caracteres.'))
        if error_messages:
            raise forms.ValidationError(error_messages)
        return mensagem
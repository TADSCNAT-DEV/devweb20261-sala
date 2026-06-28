from django import forms


class AutoregistroForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Seu nome completo'}),
    )
    username = forms.CharField(
        label='Usuário',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Escolha um usuário'}),
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Seu melhor e-mail'}),
    )
    cpf = forms.CharField(
        label='CPF',
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Somente números'}),
    )
    password = forms.CharField(
        label='Senha',
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Crie uma senha'}),
    )
    password_confirm = forms.CharField(
        label='Confirmar senha',
        min_length=8,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Repita a senha'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'As senhas não coincidem.')
        return cleaned_data


class PerfilUsuarioForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Seu nome completo'}),
    )
    username = forms.CharField(
        label='Usuário',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome de usuário', 'readonly': 'readonly'}),
    )
    email = forms.EmailField(
        label='E-mail',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'E-mail de acesso', 'readonly': 'readonly'}),
    )
    password = forms.CharField(
        label='Senha',
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Nova senha (deixe em branco para não alterar)'}),
    )
    cpf = forms.CharField(
        label='CPF',
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Somente números', 'readonly': 'readonly'}),
    )
    bio = forms.CharField(
        label='Bio',
        required=False,
        widget=forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Fale um pouco sobre você'}),
    )
    avatar = forms.ImageField(
        label='Avatar',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'input'}),
    )
    comprovante_endereco = forms.FileField(
        label='Comprovante de endereço',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'input'}),
    )
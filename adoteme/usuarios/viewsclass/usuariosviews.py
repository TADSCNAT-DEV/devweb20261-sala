from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.views import View

from usuarios.forms import AutoregistroForm, PerfilUsuarioForm
from usuarios.services import UsuarioService


AUTOREGISTRO_TEMPLATE = 'usuarios/registro.html'
PERFIL_TEMPLATE = 'usuarios/perfil.html'
LOGIN_ROUTE = 'principal:login'
PERFIL_ROUTE = 'usuarios:editar_perfil'


def adicionar_erros_ao_formulario(form, erro_validacao):
	if hasattr(erro_validacao, 'message_dict'):
		for campo, mensagens in erro_validacao.message_dict.items():
			destino = campo if campo in form.fields else None
			for mensagem in mensagens:
				form.add_error(destino, mensagem)
		return

	for mensagem in erro_validacao.messages:
		form.add_error(None, mensagem)


class AutoregistroView(View):
	def get(self, request, *args, **kwargs):
		form = AutoregistroForm()
		return render(request, AUTOREGISTRO_TEMPLATE, {'form': form})

	def post(self, request, *args, **kwargs):
		form = AutoregistroForm(request.POST)
		if not form.is_valid():
			return render(request, AUTOREGISTRO_TEMPLATE, {'form': form})

		try:
			UsuarioService.criar_usuario(
				nome=form.cleaned_data['nome'],
				email=form.cleaned_data['email'],
				username=form.cleaned_data['username'],
				cpf=form.cleaned_data['cpf'],
				password=form.cleaned_data['password'],
				tipo_usuario='ADOTANTE',
			)
		except ValidationError as erro_validacao:
			adicionar_erros_ao_formulario(form, erro_validacao)
			return render(request, AUTOREGISTRO_TEMPLATE, {'form': form})

		messages.success(request, 'Cadastro realizado com sucesso. Faça login para continuar.')
		return redirect(LOGIN_ROUTE)


class EditarPerfilView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		usuario = UsuarioService.obter_usuario(request.user.id)
		if usuario.perfil:
			bio=usuario.perfil.bio
		else:
			bio=''
		form = PerfilUsuarioForm(
			initial={
				'nome': usuario.nome,
				'username': usuario.username,
				'email': usuario.email,
				'cpf': usuario.cpf,
				'bio': bio,
				'comprovante_endereco': usuario.perfil.comprovante_endereco if usuario.perfil else None,
                'avatar': usuario.perfil.avatar if usuario.perfil else None
			}
		)
		return render(request, PERFIL_TEMPLATE, {'form': form})

	def post(self, request, *args, **kwargs):
		usuario = request.user
		form = PerfilUsuarioForm(request.POST, request.FILES)
		if not form.is_valid():
			return render(request, PERFIL_TEMPLATE, {'form': form})

		try:
			password = form.cleaned_data['password'] or None
			UsuarioService.atualizar_usuario(
				usuario.id,
				nome=form.cleaned_data['nome'],
				password=password,
			)
			UsuarioService.atualizar_perfil(
				usuario.id,
				bio=form.cleaned_data['bio'],
				avatar=form.cleaned_data['avatar'],
				comprovante_endereco=form.cleaned_data['comprovante_endereco'],
			)
		except ValidationError as erro_validacao:
			adicionar_erros_ao_formulario(form, erro_validacao)
			return render(request, PERFIL_TEMPLATE, {'form': form})

		messages.success(request, 'Perfil atualizado com sucesso!')
		return redirect(PERFIL_ROUTE)

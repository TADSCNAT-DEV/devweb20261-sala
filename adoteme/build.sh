#!/usr/bin/env bash
# exit on error
set -o errexit

# Change to project directory
#cd adoteme # Diretório do projeto

# Install dependencies
pip install -r requirements_render.txt

# Collect static files
python manage.py collectstatic --noinput --settings=adoteme.settings.production # Coloque o nome do projeto

# Run migrations
python manage.py migrate --settings=adoteme.settings.production # Coloque o nome do projeto

#Cria um superusuário com a senha definida no ambiente
python manage.py runscript createsuperuser --settings=adoteme.settings.production #Coloque o nome do projeto
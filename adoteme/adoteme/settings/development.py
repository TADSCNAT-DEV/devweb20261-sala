
from .base import *

SECRET_KEY = "django-insecure-lhmqa4qaza^jv$10=$yfm8o&_%&5ado2tf_@gq88hem%s0mhf3"

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Email backend para desenvolvimento (console) - Se tiver e-mail no sistema
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configurações específicas para arquivos estáticos em desenvolvimento
# Permitir que o Gunicorn sirva arquivos estáticos via WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Para desenvolvimento, coletamos os arquivos estáticos automaticamente
import os
if not os.path.exists(BASE_DIR / 'staticfiles'):
    os.makedirs(BASE_DIR / 'staticfiles', exist_ok=True)

# Cache simples para desenvolvimento, se tiver opção de cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

if 'CODESPACE_NAME' in os.environ:
    codespace_name = os.getenv("CODESPACE_NAME")
    codespace_domain = os.getenv("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN")
    CSRF_TRUSTED_ORIGINS = [f'https://{codespace_name}-8000.{codespace_domain}','https://localhost:8000']

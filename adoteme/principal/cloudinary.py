
from django.db import models
from django.conf import settings


try:
    from cloudinary.models import CloudinaryField
    CLOUDINARY_AVAILABLE = True
except ImportError:
    CLOUDINARY_AVAILABLE = False


def get_image_field(*args, **kwargs):
    """Retorna CloudinaryField em produção ou ImageField em desenvolvimento"""
    if CLOUDINARY_AVAILABLE and not settings.DEBUG:
        # Remove o upload_to para Cloudinary e adiciona folder se necessário
        if 'upload_to' in kwargs:
            folder = kwargs.pop('upload_to').rstrip('/')
            if 'folder' not in kwargs:
                kwargs['folder'] = f'adoteme/{folder}'
        return CloudinaryField(*args, **kwargs)
    else:
        return models.ImageField(*args, **kwargs)

def get_file_field(*args, **kwargs):
    """Retorna CloudinaryField em produção ou FileField em desenvolvimento"""
    if CLOUDINARY_AVAILABLE and not settings.DEBUG:
        # Remove o upload_to para Cloudinary e adiciona folder se necessário
        if 'upload_to' in kwargs:
            folder = kwargs.pop('upload_to').rstrip('/')
            if 'folder' not in kwargs:
                kwargs['folder'] = f'adoteme/{folder}'
        kwargs['resource_type'] = 'auto'  # Para aceitar qualquer tipo de arquivo
        return CloudinaryField(*args, **kwargs)
    else:
        return models.FileField(*args, **kwargs)
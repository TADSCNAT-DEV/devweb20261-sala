from django.contrib import admin
from leilao.models import Leilao,ItemLeilao,Lance,Participante
# Register your models here.

admin.site.register(Leilao)
admin.site.register(ItemLeilao)
admin.site.register(Lance)
admin.site.register(Participante)

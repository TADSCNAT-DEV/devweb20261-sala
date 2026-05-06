from django.contrib import admin

from animais.models import Animal, TipoAnimal, Raca

# Register your models here.

admin.site.register(Animal)
admin.site.register(TipoAnimal)
admin.site.register(Raca)
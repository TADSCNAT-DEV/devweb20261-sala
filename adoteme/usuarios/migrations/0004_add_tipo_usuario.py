# Gerado manualmente

from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0003_remove_usuario_tipo"),
    ]
    
    operations = [
        
        migrations.AddField(
            model_name="usuario",
            name="tipo_usuario",
            field= models.CharField(choices=[('ADOTANTE', 'ADOTANTE'), ('ABRIGO', 'ABRIGO')], default='ADOTANTE', max_length=20)
        )
    ]

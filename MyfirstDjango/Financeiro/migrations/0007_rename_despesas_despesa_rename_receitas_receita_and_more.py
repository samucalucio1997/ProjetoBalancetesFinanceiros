# Generated by Django 4.0.6 on 2023-12-04 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Financeiro', '0006_remove_usuario_nome_remove_usuario_senha'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Despesas',
            new_name='Despesa',
        ),
        migrations.RenameModel(
            old_name='Receitas',
            new_name='Receita',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

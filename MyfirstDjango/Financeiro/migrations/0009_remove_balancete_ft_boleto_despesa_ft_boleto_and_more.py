# Generated by Django 4.0.6 on 2023-12-09 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Financeiro', '0008_usuario_data_nasc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balancete',
            name='ft_boleto',
        ),
        migrations.AddField(
            model_name='despesa',
            name='ft_boleto',
            field=models.ImageField(blank=True, null=True, upload_to='Despesas_img/'),
        ),
        migrations.AddField(
            model_name='receita',
            name='ft_boleto',
            field=models.ImageField(blank=True, null=True, upload_to='Receitas_img/'),
        ),
    ]

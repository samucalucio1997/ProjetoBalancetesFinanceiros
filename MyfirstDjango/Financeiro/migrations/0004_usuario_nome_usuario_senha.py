# Generated by Django 4.0.6 on 2023-12-01 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Financeiro', '0003_despesas_data_receitas_data_alter_balancete_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='Jonka', max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default='jhasfdhvbakhs', max_length=100),
        ),
    ]

# Generated by Django 4.0.6 on 2023-12-02 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Financeiro', '0005_rename_login_usuario_user_remove_usuario_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
    ]

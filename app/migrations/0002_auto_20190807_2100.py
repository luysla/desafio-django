# Generated by Django 2.2.4 on 2019-08-08 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidato',
            old_name='idVaga',
            new_name='vaga',
        ),
        migrations.RenameField(
            model_name='vaga',
            old_name='idCargo',
            new_name='cargo',
        ),
    ]

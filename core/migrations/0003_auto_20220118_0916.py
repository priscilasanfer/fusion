# Generated by Django 2.2.25 on 2022-01-18 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220118_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='image',
            new_name='imagem',
        ),
    ]
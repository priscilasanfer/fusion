# Generated by Django 2.2.25 on 2022-01-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220118_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Computador'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Icone'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-09-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_alter_arriendo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='creado',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='arriendo',
            name='modificado',
            field=models.DateField(auto_now=True),
        ),
    ]
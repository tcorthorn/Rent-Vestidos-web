# Generated by Django 4.0.4 on 2022-09-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_alter_arriendo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='status',
            field=models.CharField(blank=True, choices=[('arrendado', 'Arrendado')], default='mantencion', help_text='Disponibilidad del vestido', max_length=15),
        ),
    ]

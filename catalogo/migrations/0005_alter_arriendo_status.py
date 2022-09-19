# Generated by Django 4.0.4 on 2022-09-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_alter_cliente_rut_alter_vestido_reservado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='status',
            field=models.CharField(blank=True, choices=[('arrendado', 'arrendado')], default='mantencion', help_text='Disponibilidad del vestido', max_length=15),
        ),
    ]

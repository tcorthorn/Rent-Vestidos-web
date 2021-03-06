# Generated by Django 4.0.2 on 2022-06-02 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vestido',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.cliente'),
        ),
        migrations.AddField(
            model_name='vestido',
            name='fecha_reservada',
            field=models.DateField(default='2022-05-23'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arriendo',
            name='cliente',
            field=models.ManyToManyField(help_text='Seleccione el cliente que arrienda', to='catalogo.Cliente'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='cliente',
            field=models.ManyToManyField(help_text='Ingrese cliente que pagó', to='catalogo.Cliente'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='cliente',
            field=models.ManyToManyField(to='catalogo.Cliente'),
        ),
    ]

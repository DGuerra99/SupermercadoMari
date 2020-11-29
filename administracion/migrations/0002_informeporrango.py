# Generated by Django 3.1.3 on 2020-11-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformePorRango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_dev', models.CharField(choices=[('General', 'General'), ('Compra', 'Compra'), ('Venta', 'Venta')], default='General', max_length=7, verbose_name='Tipo de Informe')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha De Inicio')),
                ('fecha_limite', models.DateField(verbose_name='Fecha De Limite')),
                ('total_compras', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Total Ventas')),
            ],
            options={
                'verbose_name': 'Informe Por Rango de Fecha',
                'verbose_name_plural': 'Informes Por Rango de Fecha',
                'db_table': 'informe_por_rango',
            },
        ),
    ]

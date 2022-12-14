# Generated by Django 4.1.2 on 2022-11-16 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empresa', models.CharField(max_length=50)),
                ('valor_empresa', models.FloatField()),
                ('valor_accion', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Raices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=50)),
                ('metros', models.IntegerField()),
                ('valor', models.FloatField()),
                ('ubicacion', models.CharField(max_length=50)),
            ],
        ),
    ]

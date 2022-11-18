# Generated by Django 4.1.2 on 2022-11-18 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfinancial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crypto',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='crypto',
            name='valor',
        ),
        migrations.AddField(
            model_name='crypto',
            name='market_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crypto',
            name='number_of_coins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crypto',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

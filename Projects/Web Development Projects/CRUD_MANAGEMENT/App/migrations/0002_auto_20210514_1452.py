# Generated by Django 3.2.3 on 2021-05-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='DBMS',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='marks',
            name='LinearAlgebra',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='marks',
            name='SWE',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='marks',
            name='computerNetworks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='marks',
            name='operatingSystems',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='marks',
            name='stats',
            field=models.FloatField(),
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-14 09:03

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('Rollno', models.IntegerField()),
                ('phoneNum', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNum', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('childName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.student')),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operatingSystems', models.BooleanField()),
                ('computerNetworks', models.BooleanField()),
                ('DBMS', models.BooleanField()),
                ('SWE', models.BooleanField()),
                ('stats', models.BooleanField()),
                ('LinearAlgebra', models.BooleanField()),
                ('studentName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.student')),
            ],
        ),
    ]
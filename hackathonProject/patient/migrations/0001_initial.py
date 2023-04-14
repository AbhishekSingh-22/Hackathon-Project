# Generated by Django 4.1.7 on 2023-04-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patientform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('age', models.IntegerField(default='')),
                ('height', models.IntegerField(default='', null=True)),
                ('weight', models.IntegerField(default='', null=True)),
                ('bloodgrp', models.CharField(default='', max_length=10)),
                ('gender', models.CharField(default='', max_length=20)),
                ('pemail', models.EmailField(default='', max_length=50)),
                ('contact', models.IntegerField(default='')),
                ('state', models.CharField(default='', max_length=50)),
                ('allergy', models.CharField(default='', max_length=20)),
                ('goingonMedications', models.CharField(default='', max_length=20)),
                ('insurance', models.CharField(default='', max_length=20)),
                ('drughistory', models.CharField(default='', max_length=50)),
                ('symptoms', models.CharField(default='', max_length=100)),
                ('medicalhistory', models.CharField(default='', max_length=100)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_alter_patientform_bloodgrp_alter_patientform_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientform',
            name='state',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
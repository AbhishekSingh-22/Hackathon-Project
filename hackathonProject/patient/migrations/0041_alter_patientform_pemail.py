# Generated by Django 4.1.7 on 2023-04-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0040_patientform_date_patientform_dusername_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientform',
            name='pemail',
            field=models.EmailField(default='', max_length=50, null=True),
        ),
    ]

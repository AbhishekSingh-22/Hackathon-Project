# Generated by Django 4.1.7 on 2023-04-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_alter_patientform_allergy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientform',
            name='pusername',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patientform',
            name='fname',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patientform',
            name='lname',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
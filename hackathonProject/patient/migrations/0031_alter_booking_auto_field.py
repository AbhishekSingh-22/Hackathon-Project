# Generated by Django 4.1.7 on 2023-04-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0030_alter_booking_auto_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='auto_field',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
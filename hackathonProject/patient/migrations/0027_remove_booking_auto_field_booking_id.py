# Generated by Django 4.1.7 on 2023-04-13 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0026_remove_booking_id_booking_auto_field_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='auto_field',
        ),
        migrations.AddField(
            model_name='booking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

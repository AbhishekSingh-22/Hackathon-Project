# Generated by Django 4.1.7 on 2023-04-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0034_datewise_slot_delete_slot_booking_slotnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='datewise_slot',
            name='doc_username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

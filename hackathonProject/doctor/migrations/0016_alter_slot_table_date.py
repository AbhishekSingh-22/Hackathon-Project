# Generated by Django 4.1.7 on 2023-04-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0015_rename_slot_slot_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot_table',
            name='date',
            field=models.DateField(null=True),
        ),
    ]

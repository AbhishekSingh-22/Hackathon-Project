# Generated by Django 4.1.7 on 2023-04-03 05:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0002_rename_doctor_doctordetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='doctordetails',
            new_name='doctordetail',
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0032_remove_booking_id_alter_booking_auto_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_username', models.CharField(max_length=50, null=True)),
                ('slotDict', models.CharField(default='', max_length=500, null=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
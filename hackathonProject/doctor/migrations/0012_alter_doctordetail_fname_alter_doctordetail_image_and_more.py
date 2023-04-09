# Generated by Django 4.1.7 on 2023-04-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_doctordetail_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetail',
            name='fname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='image',
            field=models.ImageField(default='', upload_to='doctor/images'),
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='license',
            field=models.FileField(default='', upload_to='doctor/files'),
        ),
        migrations.AlterField(
            model_name='doctordetail',
            name='specdegree',
            field=models.FileField(default='', upload_to='doctor/files'),
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-28 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_auto_20181224_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='photo',
            field=models.ImageField(default='1.jpg', upload_to='empl_photo'),
        ),
    ]

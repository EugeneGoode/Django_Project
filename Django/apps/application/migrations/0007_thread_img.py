# Generated by Django 3.0.4 on 2020-03-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_board_board_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='img',
            field=models.ImageField(default=0, upload_to='', verbose_name='Изображение'),
        ),
    ]

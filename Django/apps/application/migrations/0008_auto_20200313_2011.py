# Generated by Django 3.0.4 on 2020-03-13 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_thread_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='img',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]

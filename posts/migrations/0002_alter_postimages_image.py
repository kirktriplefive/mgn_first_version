# Generated by Django 3.2.7 on 2021-11-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='image',
            field=models.ImageField(upload_to='static/posts_images/', verbose_name='Изображение'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-11-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_postimages_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimages',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='Заголовок'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_picture_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]

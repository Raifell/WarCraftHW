# Generated by Django 4.2.7 on 2023-11-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
# Generated by Django 2.1.7 on 2019-03-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='tags',
            field=models.ManyToManyField(to='app_music.Tag'),
        ),
    ]
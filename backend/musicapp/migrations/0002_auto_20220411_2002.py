# Generated by Django 3.2.12 on 2022-04-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songdetails',
            name='song',
        ),
        migrations.AddField(
            model_name='ratings',
            name='artist',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.DeleteModel(
            name='SongDetails',
        ),
    ]

# Generated by Django 2.2.5 on 2021-02-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0001_initial'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='rooms',
            field=models.ManyToManyField(blank=True, to='rooms.Room'),
        ),
    ]

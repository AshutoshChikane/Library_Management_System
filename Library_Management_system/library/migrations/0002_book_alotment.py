# Generated by Django 4.1.1 on 2022-12-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='alotment',
            field=models.IntegerField(default=0),
        ),
    ]

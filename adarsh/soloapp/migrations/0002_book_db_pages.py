# Generated by Django 5.0.2 on 2024-03-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soloapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_db',
            name='pages',
            field=models.IntegerField(default=0),
        ),
    ]

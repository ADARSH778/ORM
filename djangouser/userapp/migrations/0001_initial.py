# Generated by Django 5.0.2 on 2024-03-06 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_DB',
            fields=[
                ('regno', models.IntegerField(primary_key='regno', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('DoB', models.DateField()),
                ('cgpa', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=30)),
                ('data', models.DateTimeField(blank=True)),
            ],
        ),
    ]

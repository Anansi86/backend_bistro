# Generated by Django 4.1.3 on 2022-11-10 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='cuisine',
        ),
    ]
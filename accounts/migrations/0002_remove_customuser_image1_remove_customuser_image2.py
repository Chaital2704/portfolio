# Generated by Django 5.0.1 on 2024-03-14 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='image2',
        ),
    ]

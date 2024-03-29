# Generated by Django 5.0.2 on 2024-03-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image1',
            field=models.ImageField(default='portfolio/static/images/assets/profile-pic-2.png', upload_to='pics'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image2',
            field=models.ImageField(default='portfolio/static/images/assets/profile-pic-2.png', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='degree',
            field=models.TextField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='job_role',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]

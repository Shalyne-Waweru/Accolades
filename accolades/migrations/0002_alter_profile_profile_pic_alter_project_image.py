# Generated by Django 4.0.5 on 2022-06-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accolades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='profile-images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='project-images/'),
        ),
    ]

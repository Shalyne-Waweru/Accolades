# Generated by Django 4.0.5 on 2022-06-14 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accolades', '0005_alter_rates_content_rate_alter_rates_design_rate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rates',
            name='content_average',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='design_average',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='total',
        ),
        migrations.RemoveField(
            model_name='rates',
            name='usability_average',
        ),
    ]

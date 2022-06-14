# Generated by Django 4.0.5 on 2022-06-14 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accolades', '0003_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_rate', models.IntegerField()),
                ('usability_rate', models.IntegerField()),
                ('content_rate', models.IntegerField()),
                ('design_average', models.FloatField(blank=True, default=0)),
                ('usability_average', models.FloatField(blank=True, default=0)),
                ('content_average', models.FloatField(blank=True, default=0)),
                ('total', models.FloatField(blank=True, default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='accolades.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

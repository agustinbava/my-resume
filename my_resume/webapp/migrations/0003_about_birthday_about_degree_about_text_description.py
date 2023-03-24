# Generated by Django 4.1.7 on 2023-03-24 21:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='about',
            name='degree',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='about',
            name='text_description',
            field=models.TextField(default='', max_length=25000),
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-27 21:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_description', models.TextField()),
                ('summary', models.TextField(default='', max_length=25000)),
                ('city', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('degree', models.CharField(default='', max_length=50)),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('text_description', models.TextField(default='', max_length=25000)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_description', models.TextField()),
                ('skills', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]

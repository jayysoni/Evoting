# Generated by Django 5.1.6 on 2025-03-25 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='party',
        ),
    ]

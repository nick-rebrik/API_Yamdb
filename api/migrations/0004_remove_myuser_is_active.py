# Generated by Django 3.0.5 on 2021-06-22 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_myuser_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_active',
        ),
    ]

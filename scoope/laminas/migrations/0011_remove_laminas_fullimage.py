# Generated by Django 3.2.12 on 2023-06-21 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laminas', '0010_estruturas_mascara'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laminas',
            name='fullimage',
        ),
    ]
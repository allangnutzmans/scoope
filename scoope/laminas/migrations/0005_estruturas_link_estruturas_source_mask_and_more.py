# Generated by Django 4.2.2 on 2023-06-07 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laminas', '0004_alter_estruturas_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='estruturas',
            name='link',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='estruturas',
            name='source_mask',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='laminas',
            name='fullimage',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='estruturas',
            name='nome_estrutura',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# Generated by Django 3.2.12 on 2023-06-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laminas', '0008_alter_laminas_imagem_completa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laminas',
            name='imagem_completa',
            field=models.ImageField(null=True, upload_to='imagens_laminas'),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-09 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0002_alter_mixeddrinks_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mixeddrinks',
            name='garnishes',
            field=models.TextField(default='No garnish needed.'),
        ),
    ]

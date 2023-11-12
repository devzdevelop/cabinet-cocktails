# Generated by Django 4.2.7 on 2023-11-09 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0003_mixeddrinks_garnishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedMixedDrinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cocktails.mixeddrinks')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2023-03-03 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='title', to='titles.Genre'),
        ),
    ]

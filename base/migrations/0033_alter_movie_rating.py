# Generated by Django 4.1.7 on 2023-04-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(max_length=5),
        ),
    ]

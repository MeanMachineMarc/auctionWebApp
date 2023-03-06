# Generated by Django 4.1.7 on 2023-03-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_alter_listitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='numBids',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listitem',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
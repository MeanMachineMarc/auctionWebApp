# Generated by Django 4.1.7 on 2023-04-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_item_buyer_item_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='fcmToken',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

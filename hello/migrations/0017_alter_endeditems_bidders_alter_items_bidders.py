# Generated by Django 4.1.7 on 2023-03-08 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0016_alter_endeditems_bidders_alter_items_bidders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endeditems',
            name='bidders',
            field=models.CharField(default=[], max_length=999999999),
        ),
        migrations.AlterField(
            model_name='items',
            name='bidders',
            field=models.CharField(default=[], max_length=999999999),
        ),
    ]

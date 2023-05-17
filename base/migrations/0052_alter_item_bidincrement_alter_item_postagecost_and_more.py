# Generated by Django 4.1.7 on 2023-05-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0051_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='bidIncrement',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='postageCost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]

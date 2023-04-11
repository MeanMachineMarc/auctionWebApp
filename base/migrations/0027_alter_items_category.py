# Generated by Django 4.1.7 on 2023-04-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_items_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('bOIS', 'Business, Office & Industrial Supplies'), ('hB', 'Health & Beauty'), ('f', 'Fashion'), ('e', 'Electronics'), ('hG', 'Home Garden'), ('sHL', 'Sports, Hobbies & Leisure'), ('mt', 'Motors'), ('cA', 'Collectables & Art'), ('mda', 'Media'), ('o', 'Other')], default='e', max_length=50),
        ),
    ]

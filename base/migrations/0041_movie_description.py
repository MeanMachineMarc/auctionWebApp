# Generated by Django 4.1.7 on 2023-05-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_account_fcmtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.CharField(default='Humpty Dumpty sat on a wall and had a great fall.', max_length=3000),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_logitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listitem',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='logitem',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
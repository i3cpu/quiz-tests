# Generated by Django 3.2.16 on 2023-01-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='quantity of questions'),
        ),
    ]

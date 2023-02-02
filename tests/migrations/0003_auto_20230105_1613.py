# Generated by Django 3.2.16 on 2023-01-05 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_testmodel_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='quantity of questions')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
            ],
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.testmodelcategories'),
        ),
    ]
# Generated by Django 2.0.6 on 2018-06-21 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charger',
            name='Cable_Length',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='charger',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='headset',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='Battery_Rating',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='memorycard',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='memorycard',
            name='Weight',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='Weight',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='powerbank',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='powerbank',
            name='Weight',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='Description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='Weight',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moeda',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]

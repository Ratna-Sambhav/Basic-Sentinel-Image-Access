# Generated by Django 4.1.2 on 2022-10-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_pystac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-05 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='date_ajout',
            field=models.DateField(auto_now=True),
        ),
    ]

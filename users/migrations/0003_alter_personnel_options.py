# Generated by Django 4.2.2 on 2023-07-05 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_personnel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personnel',
            options={'verbose_name': 'Personnel', 'verbose_name_plural': 'Personnels'},
        ),
    ]

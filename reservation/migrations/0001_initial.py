# Generated by Django 4.2.2 on 2023-07-05 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=50)),
                ('prenom_client', models.CharField(max_length=150)),
                ('adresse_client', models.CharField(max_length=100)),
                ('date_reservation', models.DateField(auto_now=True)),
                ('date_arrivee', models.DateField(null=True)),
                ('nombre_jours', models.IntegerField(null=True)),
                ('chambre', models.CharField(max_length=10)),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_weather'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('true_start', models.FloatField()),
                ('true_end', models.FloatField()),
                ('pred_start', models.FloatField()),
                ('pred_end', models.FloatField()),
            ],
            options={
                'db_table': 'trip_data',
                'managed': False,
            },
        ),
    ]

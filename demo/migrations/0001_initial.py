# Generated by Django 4.1.1 on 2022-09-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StationInfo',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('indexnum', models.IntegerField(blank=True, null=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('station_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'station_info',
                'managed': False,
            },
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('intro', models.TextField()),
                ('motivation', models.TextField()),
                ('model', models.TextField()),
                ('dataset', models.TextField()),
                ('experiment', models.TextField()),
            ],
        ),
    ]

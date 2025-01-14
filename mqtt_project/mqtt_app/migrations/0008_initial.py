# Generated by Django 4.2.1 on 2023-06-01 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mqtt_app', '0007_delete_indication_delete_sensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('width', models.CharField(max_length=10, null=True)),
                ('heigth', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'point',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('unit', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'sensor',
            },
        ),
        migrations.CreateModel(
            name='Indication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('width', models.CharField(max_length=10)),
                ('height', models.CharField(max_length=10)),
                ('value', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mqtt_app.sensor')),
            ],
            options={
                'db_table': 'indication',
            },
        ),
    ]

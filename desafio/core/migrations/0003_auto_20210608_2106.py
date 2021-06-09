# Generated by Django 3.1.4 on 2021-06-09 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210608_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dado',
            fields=[
                ('id_event', models.AutoField(primary_key=True, serialize=False)),
                ('date_event', models.CharField(blank=True, max_length=100, null=True)),
                ('event_type', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.CharField(blank=True, max_length=150, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'dados',
                'ordering': ['id_event'],
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
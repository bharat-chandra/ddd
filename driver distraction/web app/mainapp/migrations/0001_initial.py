# Generated by Django 3.1.4 on 2022-04-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.IntegerField()),
                ('date', models.TextField()),
                ('timestamp', models.TextField()),
                ('action', models.TextField()),
            ],
            options={
                'db_table': 'Performance',
            },
        ),
    ]

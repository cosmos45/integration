# Generated by Django 3.2 on 2021-04-19 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('no_of_cities', models.CharField(max_length=500)),
                ('no_of_days', models.CharField(max_length=500)),
                ('total_expense', models.CharField(max_length=500)),
                ('destinations', models.CharField(max_length=500)),
                ('day_overview', models.CharField(max_length=500)),
                ('image', models.ImageField(default=0, upload_to='images')),
                ('single_occupancy', models.IntegerField(default=0)),
                ('twin_sharing', models.IntegerField(default=0)),
                ('triple_sharing', models.IntegerField(default=0)),
                ('infant', models.IntegerField(default=0)),
                ('child_with_mat', models.IntegerField(default=0)),
                ('child_without_mat', models.IntegerField(default=0)),
                ('child', models.IntegerField(default=0)),
            ],
        ),
    ]

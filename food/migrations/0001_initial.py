# Generated by Django 3.2 on 2021-04-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(default=0, upload_to='images')),
                ('cost_for_2', models.CharField(max_length=500)),
                ('restaurant', models.CharField(max_length=500)),
                ('must_try', models.CharField(max_length=500)),
            ],
        ),
    ]

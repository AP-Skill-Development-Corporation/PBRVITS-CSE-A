# Generated by Django 3.0 on 2021-12-16 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stdnt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=50)),
                ('sname', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
            ],
        ),
    ]

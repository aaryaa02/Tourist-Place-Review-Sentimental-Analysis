# Generated by Django 4.1.7 on 2023-04-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datamodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
                ('Review', models.CharField(max_length=100)),
                ('Rating', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Raw_Review', models.CharField(max_length=100)),
            ],
        ),
    ]

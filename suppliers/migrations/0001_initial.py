# Generated by Django 4.2.5 on 2023-10-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=14, unique=True)),
                ('details', models.TextField(null=True)),
                ('type', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'Supplier',
            },
        ),
    ]

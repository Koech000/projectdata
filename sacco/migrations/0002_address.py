# Generated by Django 5.1.3 on 2024-11-13 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('sub_county', models.CharField(max_length=50)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='sacco.customer')),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
    ]
# Generated by Django 5.2.1 on 2025-05-25 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
        ('histories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='id_us',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='histories.histories', verbose_name='User Story'),
        ),
    ]

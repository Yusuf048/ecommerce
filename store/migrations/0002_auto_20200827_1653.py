# Generated by Django 3.1 on 2020-08-27 13:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AddField(
            model_name='customer',
            name='tcNo',
            field=models.CharField(default=0, max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]

# Generated by Django 3.1 on 2020-08-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200827_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='tcNo',
        ),
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, default=1111111111111, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

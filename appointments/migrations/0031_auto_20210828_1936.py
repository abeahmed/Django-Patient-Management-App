# Generated by Django 2.2.24 on 2021-08-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0030_auto_20210828_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=6),
        ),
    ]

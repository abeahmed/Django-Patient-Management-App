# Generated by Django 2.2.24 on 2021-08-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0029_auto_20210828_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.2.12 on 2022-07-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0010_auto_20220611_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestantform',
            name='amount',
            field=models.PositiveIntegerField(default=100),
        ),
    ]

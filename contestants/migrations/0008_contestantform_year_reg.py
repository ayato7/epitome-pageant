# Generated by Django 3.2.12 on 2022-05-18 15:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0007_remove_contestantform_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestantform',
            name='year_reg',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

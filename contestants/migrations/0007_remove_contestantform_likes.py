# Generated by Django 3.2.12 on 2022-03-28 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0006_alter_contestantform_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestantform',
            name='likes',
        ),
    ]

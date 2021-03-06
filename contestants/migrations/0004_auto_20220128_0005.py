# Generated by Django 3.2 on 2022-01-28 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestants', '0003_alter_contestantform_reg_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestantform',
            name='reg_email',
        ),
        migrations.AddField(
            model_name='contestantform',
            name='state_of_origin',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contestantform',
            name='state_of_residence',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contestantform',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]

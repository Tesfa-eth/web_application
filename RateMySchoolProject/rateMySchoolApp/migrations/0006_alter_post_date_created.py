# Generated by Django 4.0.2 on 2022-03-17 05:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rateMySchoolApp', '0005_alter_post_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 3, 17, 5, 2, 6, 747754, tzinfo=utc)),
        ),
    ]
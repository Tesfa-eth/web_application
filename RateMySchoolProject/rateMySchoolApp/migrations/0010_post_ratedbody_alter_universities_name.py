# Generated by Django 4.0.2 on 2022-03-19 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rateMySchoolApp', '0009_universities'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ratedBody',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='rateMySchoolApp.universities'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='universities',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

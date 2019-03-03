# Generated by Django 2.1.5 on 2019-03-01 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20190301_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name_ko',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]

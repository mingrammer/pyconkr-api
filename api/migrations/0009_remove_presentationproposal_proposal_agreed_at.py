# Generated by Django 2.1.5 on 2019-03-16 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190316_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentationproposal',
            name='proposal_agreed_at',
        ),
    ]

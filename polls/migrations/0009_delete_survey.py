# Generated by Django 2.2.6 on 2019-10-24 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_survey'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Survey',
        ),
    ]

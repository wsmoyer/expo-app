# Generated by Django 2.2.6 on 2019-10-24 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20191024_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='response',
        ),
        migrations.AddField(
            model_name='response',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]

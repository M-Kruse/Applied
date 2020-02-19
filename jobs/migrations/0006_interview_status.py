# Generated by Django 2.2.10 on 2020-02-18 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200218_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='status',
            field=models.CharField(choices=[('OF', 'OFFERED'), ('SC', 'SCHEDULED'), ('CL', 'COMPLETED')], default='', max_length=12),
        ),
    ]

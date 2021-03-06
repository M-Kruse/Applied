# Generated by Django 2.2.10 on 2020-03-05 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20200304_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='summary',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='template',
            name='type',
            field=models.CharField(choices=[('R', 'Resume'), ('C', 'Cover Letter')], default='RESUME', max_length=64),
        ),
    ]

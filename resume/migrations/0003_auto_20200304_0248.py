# Generated by Django 2.2.10 on 2020-03-04 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20200304_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='template_type',
            new_name='type',
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-18 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_auto_20191017_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dogpost',
            old_name='namedog',
            new_name='servicio',
        ),
        migrations.RenameField(
            model_name='dogpost',
            old_name='rutdueño',
            new_name='user',
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-09 14:53

from django.db import migrations, models
import fixpol.models


class Migration(migrations.Migration):

    dependencies = [
        ('fixpol', '0020_auto_20200809_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='law',
            name='key',
            field=models.CharField(default=fixpol.models.get_default_law_key, max_length=20, unique=True),
        ),
    ]

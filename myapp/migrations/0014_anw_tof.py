# Generated by Django 4.0.1 on 2022-02-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_anw'),
    ]

    operations = [
        migrations.AddField(
            model_name='anw',
            name='tof',
            field=models.BooleanField(default=True, verbose_name='是否正确'),
            preserve_default=False,
        ),
    ]

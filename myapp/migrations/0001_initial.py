# Generated by Django 4.0.1 on 2022-01-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=10)),
                ('user_password', models.IntegerField()),
                ('user_type', models.IntegerField()),
            ],
        ),
    ]
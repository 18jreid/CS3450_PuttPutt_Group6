# Generated by Django 3.1.7 on 2021-09-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=14)),
                ('password', models.CharField(max_length=21)),
                ('account_balance', models.FloatField(default=0)),
            ],
        ),
    ]

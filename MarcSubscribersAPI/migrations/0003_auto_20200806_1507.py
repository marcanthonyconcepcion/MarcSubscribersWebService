# Generated by Django 3.1 on 2020-08-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarcSubscribersAPI', '0002_auto_20200806_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='first_name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='last_name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]

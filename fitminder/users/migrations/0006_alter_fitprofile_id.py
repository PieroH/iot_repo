# Generated by Django 3.2.5 on 2021-07-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210316_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

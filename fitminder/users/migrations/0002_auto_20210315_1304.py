# Generated by Django 3.1.5 on 2021-03-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitprofile',
            name='img',
            field=models.ImageField(default='profile.jpg', upload_to='media/fit_profile_pic'),
        ),
    ]

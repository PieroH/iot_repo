# Generated by Django 3.2.5 on 2021-07-28 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitfeed', '0002_auto_20210722_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='message',
            field=models.TextField(default='', verbose_name='Message'),
        ),
    ]
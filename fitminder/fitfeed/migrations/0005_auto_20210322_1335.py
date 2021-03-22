# Generated by Django 3.1.5 on 2021-03-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitfeed', '0004_auto_20210316_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='author',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='content',
        ),
        migrations.AddField(
            model_name='feed',
            name='instruction',
            field=models.CharField(default='', max_length=600),
        ),
        migrations.AddField(
            model_name='feed',
            name='intensity',
            field=models.CharField(choices=[('..1', 'LOW'), ('..2', 'MODERATE'), ('..3', 'HIGH'), ('..4', '...')], default='..4', max_length=3),
        ),
        migrations.AddField(
            model_name='feed',
            name='preparation',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='feed',
            name='duration',
            field=models.DurationField(null=True),
        ),
    ]

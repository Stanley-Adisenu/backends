# Generated by Django 5.0.3 on 2024-05-15 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201126_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='bio',
            field=models.TextField(blank=True, default=' ', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='department',
            field=models.CharField(blank=True, default=' ', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='full_name',
            field=models.CharField(blank=True, default=models.CharField(default='Student', max_length=255, unique=True), max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user_name',
            field=models.CharField(default='Student', max_length=255, unique=True),
        ),
    ]

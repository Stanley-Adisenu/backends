# Generated by Django 5.0.3 on 2024-07-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_message_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='total_points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

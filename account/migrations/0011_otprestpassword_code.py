# Generated by Django 4.2.1 on 2023-11-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_otprestpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='otprestpassword',
            name='code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]

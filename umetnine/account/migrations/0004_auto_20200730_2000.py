# Generated by Django 3.0.8 on 2020-07-30 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200729_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='country',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-26 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artists', '0003_delete_artworklikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arts',
            name='liked_by',
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Arts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

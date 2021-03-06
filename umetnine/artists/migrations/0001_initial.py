# Generated by Django 3.0.8 on 2020-08-25 13:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField()),
                ('likes', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stili',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('stil', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Umetnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year_of_birth', models.DateField(verbose_name='birth')),
                ('year_of_death', models.DateField(verbose_name='death')),
                ('nationality', models.CharField(max_length=200)),
                ('group', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Umetnina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2020)])),
                ('style', models.CharField(max_length=200)),
                ('technique', models.CharField(max_length=200)),
                ('medium', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Umetnik')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.CharField(max_length=200)),
                ('artwork_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Arts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArtworksTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Arts')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Tags')),
            ],
        ),
    ]

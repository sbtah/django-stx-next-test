# Generated by Django 3.2 on 2021-09-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('author', models.CharField(blank=True, max_length=120, null=True)),
                ('date_published', models.CharField(blank=True, max_length=12, null=True)),
                ('isbn_number', models.CharField(blank=True, max_length=120, null=True)),
                ('number_of_pages', models.PositiveIntegerField(blank=True, null=True)),
                ('link_to_cover', models.URLField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-05 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=50, verbose_name='NAME')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='DATE')),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark.bookmarklist')),
            ],
        ),
    ]
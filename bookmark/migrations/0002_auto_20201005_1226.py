# Generated by Django 3.1.1 on 2020-10-05 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookmarkList',
            new_name='BookmarkSet',
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-12 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_rename_date_created_like_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='available_accounts',
            new_name='available_blogs',
        ),
    ]

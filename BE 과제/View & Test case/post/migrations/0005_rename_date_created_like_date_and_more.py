# Generated by Django 4.2.1 on 2023-05-12 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_blog_available_accounts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='date_created',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='date_created',
            new_name='date',
        ),
    ]

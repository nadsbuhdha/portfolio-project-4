# Generated by Django 3.2 on 2022-04-15 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_albumreview_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_body',
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-26 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0002_catergory_icecream_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catergory',
            new_name='Category',
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icecream', '0004_category_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
                ('icecreams', models.ManyToManyField(to='icecream.icecream')),
            ],
        ),
    ]
# Generated by Django 4.1.5 on 2023-02-09 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['publish_date']},
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-01 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_source_title_alter_source_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time_step',
            name='title',
        ),
    ]

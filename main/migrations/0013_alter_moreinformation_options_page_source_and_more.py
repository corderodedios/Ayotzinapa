# Generated by Django 4.2.1 on 2023-06-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_moreinformation_remove_source_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moreinformation',
            options={'verbose_name': 'Mehr Informationen', 'verbose_name_plural': 'Mehr Informationen'},
        ),
        migrations.AddField(
            model_name='page',
            name='source',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='victim',
            name='identified',
            field=models.BooleanField(default=False),
        ),
    ]

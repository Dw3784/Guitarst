# Generated by Django 5.0.2 on 2024-04-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_categories_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='url_name',
            field=models.TextField(blank=True, max_length=25, null=True),
        ),
    ]

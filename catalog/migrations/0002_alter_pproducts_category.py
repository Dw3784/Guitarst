# Generated by Django 5.0.2 on 2024-03-31 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pproducts',
            name='category',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
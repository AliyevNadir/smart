# Generated by Django 5.1.2 on 2024-10-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_category_slug_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

# Generated by Django 4.1.4 on 2023-04-18 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category_comments_item_raiting_salesman_salesmans_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Salesman',
        ),
    ]
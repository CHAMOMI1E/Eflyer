# Generated by Django 4.1.4 on 2023-04-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_users_basket_alter_basket_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=100),
        ),
        migrations.RemoveField(
            model_name='basket',
            name='items',
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='basket',
            name='items',
            field=models.ManyToManyField(to='app.item'),
        ),
    ]

# Generated by Django 4.2.6 on 2024-04-20 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_products_alter_sqtable_cont_msg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='psize',
        ),
    ]

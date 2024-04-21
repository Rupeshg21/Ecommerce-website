# Generated by Django 4.2.6 on 2024-04-21 11:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
            ],
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default='exit', on_delete=django.db.models.deletion.CASCADE, to='app.cartt'),
            preserve_default=False,
        ),
    ]

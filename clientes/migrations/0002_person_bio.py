# Generated by Django 4.1.7 on 2023-03-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]

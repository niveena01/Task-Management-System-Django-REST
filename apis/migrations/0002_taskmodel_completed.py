# Generated by Django 4.2.2 on 2023-10-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]

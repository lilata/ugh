# Generated by Django 3.2.12 on 2022-02-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iloveme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='body_title',
            field=models.TextField(default=''),
        ),
    ]

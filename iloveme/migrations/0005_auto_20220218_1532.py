# Generated by Django 3.2.12 on 2022-02-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iloveme', '0004_page_pic_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='summary',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='body_title',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_title',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='pic_alt',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='page',
            name='pic_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

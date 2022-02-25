# Generated by Django 3.2.12 on 2022-02-18 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iloveme', '0002_page_body_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='pic_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='navlink',
            name='text',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='ProfileTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('tag', models.CharField(max_length=100)),
                ('value', models.TextField(default='')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iloveme.page')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

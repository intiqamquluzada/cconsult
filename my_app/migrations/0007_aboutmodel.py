# Generated by Django 4.2.7 on 2023-11-15 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_comment_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('sub_title', models.CharField(max_length=255, verbose_name='Sub title')),
                ('description', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
                'ordering': ('-created_at',),
            },
        ),
    ]